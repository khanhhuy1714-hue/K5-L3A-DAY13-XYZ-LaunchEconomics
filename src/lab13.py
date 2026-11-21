"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Toàn bộ dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000  # đồng / tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong (0, 1]')
    if k is None:
        return 1.0 / p
    if k < 1:
        raise ValueError('k phải là số nguyên dương')
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 <= p <= 1:
        raise ValueError('p phải nằm trong [0, 1]')
    if k is None:
        return 1.0
    if k < 1:
        raise ValueError('k phải là số nguyên dương')
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'].astype(int) > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    chay_lai = float((tien_token + tien_tool)[runs['attempt'] > 1].sum())
    xem_lai = float(reqs['phut_xem_lai_simulated'].astype(float).sum() * luong_phut * he_so_xem_lai)
    lam_lai = float(reqs['phut_lam_lai_simulated'].astype(float).sum() * luong_phut * he_so_lam_lai)

    token_sum = float(tien_token.sum())
    tool_sum = float(tien_tool.sum())
    tong = token_sum + tool_sum + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    cps = math.inf if thanh_cong == 0 else tong / thanh_cong
    return dict(
        token=token_sum,
        tool=tool_sum,
        chay_lai=chay_lai,
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=float(cps),
        hoa_don_moi_yc=(token_sum + tool_sum) / len(reqs) if len(reqs) else 0.0,
    )


def co_mau_hai_ti_le(p1, p2, alpha=0.05, power=0.80):
    """Cỡ mẫu mỗi nhóm theo công thức chuẩn so sánh hai tỉ lệ."""
    za = NormalDist().inv_cdf(1.0 - alpha / 2.0)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2.0
    num = (za * math.sqrt(2.0 * pb * (1.0 - pb)) + zb * math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))) ** 2
    return math.ceil(num / ((p2 - p1) ** 2))


def in_nhiem_vu_a(runs, reqs):
    """In kết quả A2, A3, A4."""
    print('\n=== A2 · Mô hình chi phí từ trace ===')
    kq = mo_hinh(runs, reqs)
    for ten, gia_tri in kq.items():
        if ten == 'hoa_don_moi_yc':
            print(f'{ten:16s} {gia_tri:>14,.1f}')
        else:
            print(f'{ten:16s} {gia_tri:>14,.0f}')
    ty_so = kq['cps'] / kq['hoa_don_moi_yc']
    khong_tc = len(reqs) - kq['thanh_cong']
    he_thong_moi_yc = (kq['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Tỉ số CPS / hoá đơn: {ty_so:.1f} lần (simulated)')
    print(f'Tỉ trọng: làm lại {kq["lam_lai"] / kq["tong"] * 100:.1f}%, xem lại {kq["xem_lai"] / kq["tong"] * 100:.1f}% (simulated)')
    print(f'Chi phí cả hệ thống/yêu cầu (cộng {khong_tc} ca * 12.000): {he_thong_moi_yc:,.0f} đ ({he_thong_moi_yc / BASELINE:.2f}x, simulated)')

    print('\n=== A3 · Tách theo loại yêu cầu ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, sub)
        ty_le_tc = r['thanh_cong'] / len(sub) * 100.0
        lan_chay_tb = sub['so_lan_chay'].astype(int).mean()
        print(f'{loai:10s} | n={len(sub):3d} | tc={r["thanh_cong"]:3d} ({ty_le_tc:5.1f}%) | chạy/yc={lan_chay_tb:.2f} | cps={r["cps"]:>7,.0f} đ ({r["cps"] / BASELINE:.2f}x, simulated)')

    print('\n--- Tỉ lệ lần chạy status == ok theo loại và attempt ---')
    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['is_ok'] = (merged['status'] == 'ok').astype(float)
    piv = merged.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100.0
    print(piv.round(1))

    print('\n=== A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ===')
    sub_pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r_pv = mo_hinh(runs, sub_pv)
    viec_tc_thang = 45000.0 * r_pv['thanh_cong'] / len(reqs)
    co_dinh_full = CHI_PHI_CO_DINH_THANG / viec_tc_thang
    cps_full = r_pv['cps'] + co_dinh_full
    co_dinh_half = CHI_PHI_CO_DINH_THANG / (viec_tc_thang / 2.0)
    cps_half = r_pv['cps'] + co_dinh_half
    print(f'Biến đổi phạm vi: {r_pv["cps"]:,.0f} đ ({r_pv["thanh_cong"]} việc tc / {len(sub_pv)} yc, simulated)')
    print(f'45.000 yc/tháng: {viec_tc_thang:,.0f} việc tc | cố định {co_dinh_full:,.0f} đ | tổng {cps_full:,.0f} đ ({cps_full / BASELINE:.2f}x, simulated)')
    print(f'Nửa khối lượng : {viec_tc_thang / 2:,.0f} việc tc | cố định {co_dinh_half:,.0f} đ | tổng {cps_half:,.0f} đ ({cps_half / BASELINE:.2f}x, simulated)')
    return kq


def in_nhiem_vu_b(runs, reqs, goc):
    """In kết quả B1, B2, B3, B4."""
    print('\n=== B1 & B2 · Bảng độ nhạy ===')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    cps_goc = goc['cps']
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:28s} {cps:8,.0f} đ ({(cps / cps_goc - 1.0) * 100:+6.1f}%, simulated)')

    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f'{"Token x2 + Xem lại x2 (B2)":28s} {cps_cap:8,.0f} đ ({(cps_cap / cps_goc - 1.0) * 100:+6.1f}%, simulated)')

    print('\n=== B3 · Giới hạn chạy lại và chi phí cả hệ thống ===')
    for m in [1, 2, 3]:
        r = mo_hinh(runs, reqs, max_lan_chay=m)
        khong_tc = len(reqs) - r['thanh_cong']
        ca_he_thong = r['tong'] + khong_tc * BASELINE
        print(f'Giới hạn {m} lần | trợ lý={r["tong"]:>10,.0f} đ | không tc={khong_tc:3d} | hệ thống={ca_he_thong:>10,.0f} đ | cps={r["cps"]:,.0f} đ (simulated)')

    print('\n=== B4 · Xem lại 100% (phạm vi noi_dia + hang_nang) ===')
    sub_pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r_pv = mo_hinh(runs, sub_pv)
    runs_pv = runs[runs['request_id'].isin(sub_pv['request_id'])]
    so_yc_co_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_ca_lam_lai = int((sub_pv['ket_qua'] == 'lam_lai').sum())
    tok_tool_pv = r_pv['token'] + r_pv['tool']
    tong_9p = so_yc_co_ok * 5 * LUONG_PHUT + so_ca_lam_lai * 9 * LUONG_PHUT + tok_tool_pv
    cps_9p = tong_9p / r_pv['thanh_cong']
    tb_phut_ll = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].astype(float).mean()
    tong_tb = so_yc_co_ok * 5 * LUONG_PHUT + so_ca_lam_lai * tb_phut_ll * LUONG_PHUT + tok_tool_pv
    cps_tb = tong_tb / r_pv['thanh_cong']
    hoa_von_9p = (r_pv['thanh_cong'] * BASELINE - so_ca_lam_lai * 9 * LUONG_PHUT - tok_tool_pv) / (so_yc_co_ok * LUONG_PHUT)
    hoa_von_tb = (r_pv['thanh_cong'] * BASELINE - so_ca_lam_lai * tb_phut_ll * LUONG_PHUT - tok_tool_pv) / (so_yc_co_ok * LUONG_PHUT)
    print(f'{so_yc_co_ok} ok, {so_ca_lam_lai} làm lại | 9 phút/ca -> {cps_9p:,.0f} đ ({cps_9p / BASELINE:.2f}x, simulated), hoà vốn <= {hoa_von_9p:.2f} phút')
    print(f'Trung bình dữ liệu {tb_phut_ll:.1f} phút/ca -> {cps_tb:,.0f} đ ({cps_tb / BASELINE:.2f}x, simulated), hoà vốn <= {hoa_von_tb:.2f} phút')


def in_nhiem_vu_d_e(reqs):
    """In kết quả D1 (cỡ mẫu), tỉ lệ an toàn nền và E1."""
    print('\n=== D1 · Cỡ mẫu & thiết kế cụm (alpha=0.05, power=0.80, ICC=0.02) ===')
    n_5pp = co_mau_hai_ti_le(0.70, 0.75)
    n_sm_5pp = math.ceil(NormalIndPower().solve_power(effect_size=proportion_effectsize(0.70, 0.75), alpha=0.05, power=0.80))
    de_75 = 1.0 + (75 - 1) * 0.02
    n_75 = math.ceil(n_5pp * de_75)
    nhan_vien_can = math.ceil(n_75 / 75)
    n_eff_20 = 20 / 0.02
    n_eff_6 = 6 / 0.02
    n_6pp = co_mau_hai_ti_le(0.70, 0.76)
    m_min = math.ceil(n_6pp * 0.98 / (20 - n_6pp * 0.02))
    de_m299 = 1.0 + (m_min - 1) * 0.02
    power_5pp_tai_859 = NormalIndPower().solve_power(effect_size=proportion_effectsize(0.70, 0.75), nobs1=859, alpha=0.05)

    print(f'a) Theo yêu cầu (+5 điểm): {n_5pp} yc/nhóm (statsmodels h-method: {n_sm_5pp})')
    print(f'b) Theo nhân viên m=75: DE={de_75:.2f}, cần {n_75} yc/nhóm -> {nhan_vien_can} người/nhóm (tổng {nhan_vien_can * 2} > 40)')
    print(f'c) 20 nhân viên/nhóm: n_hiệu_dụng tối đa = {n_eff_20:.0f} < {n_5pp} (không đạt 5 điểm)')
    print(f'd) 6 depot/nhóm: n_hiệu_dụng tối đa = {n_eff_6:.0f} < {n_5pp}')
    print(f'e) Mức chênh 6 điểm (n={n_6pp}/nhóm), 20 nhân viên/nhóm: m >= {m_min} yc/người (DE={de_m299:.2f})')
    print(f'   Đánh đổi: power tại mức 5 điểm với n_eff={n_6pp} chỉ còn {power_5pp_tai_859:.2f}')

    sub_pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    print(f'Tỉ lệ mo_lai_trong_7_ngay: toàn bộ={reqs["mo_lai_trong_7_ngay"].mean() * 100:.2f}% | phạm vi={sub_pv["mo_lai_trong_7_ngay"].mean() * 100:.2f}%')

    print('\n=== E1 · Tính thử 3 chỉ số trên 1.200 yêu cầu ===')
    chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).mean() * 100.0
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).mean() * 100.0
    an_toan = (reqs['mo_lai_trong_7_ngay'] == 1).mean() * 100.0
    chinh_cnt = int(((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum())
    print(f'Chính (đóng 24h, không mở lại 7 ngày): {chinh:.2f}% ({chinh_cnt}/{len(reqs)})')
    print(f'Dùng (bỏ qua gợi ý sua + bo): {bo_qua:.2f}% ({int(xem["quyet_dinh_xem_lai"].isin(["sua", "bo"]).sum())}/{len(xem)})')
    print(f'An toàn (mở lại trong 7 ngày): {an_toan:.2f}% ({int((reqs["mo_lai_trong_7_ngay"] == 1).sum())}/{len(reqs)})')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    goc = in_nhiem_vu_a(runs, reqs)
    in_nhiem_vu_b(runs, reqs, goc)
    in_nhiem_vu_d_e(reqs)
