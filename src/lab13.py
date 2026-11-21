"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if not 0 < p <= 1:
        raise ValueError('p phải nằm trong (0, 1]')
    if k is None:
        return 1 / p
    if k < 1:
        raise ValueError('k phải là số nguyên dương')
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if not 0 <= p <= 1:
        raise ValueError('p phải nằm trong [0, 1]')
    if k is None:
        return 1.0
    if k < 1:
        raise ValueError('k phải là số nguyên dương')
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    success = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / success


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
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

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].astype(float).sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].astype(float).sum() * luong_phut * he_so_lam_lai
    token = float(tien_token.sum())
    tool = float(tien_tool.sum())
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    tong = token + tool + xem_lai + lam_lai
    if thanh_cong == 0:
        cps = math.inf
    else:
        cps = tong / thanh_cong
    return dict(token=token, tool=tool,
                chay_lai=float((tien_token + tien_tool)[runs['attempt'] > 1].sum()),
                xem_lai=float(xem_lai), lam_lai=float(lam_lai), tong=float(tong),
                thanh_cong=thanh_cong, cps=float(cps),
                hoa_don_moi_yc=(token + tool) / len(reqs) if len(reqs) else 0.0)


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\nA2 · Toàn bộ mẫu')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:20s} {gia_tri:>14,.2f}' if isinstance(gia_tri, float) else f'{ten:20s} {gia_tri:>14,}')
    print(f"CPS / hóa đơn token+tool mỗi yêu cầu: {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.2f}x")

    # A3 · Tách theo loại yêu cầu.
    print('\nA3 · Theo loại')
    print('loai         so_yc  thanh_cong  ti_le_tc  lan_chay/yc  cps      /12.000')
    for loai in reqs['loai'].drop_duplicates():
        subset = reqs[reqs['loai'] == loai]
        model = mo_hinh(runs, subset)
        print(f"{loai:12s} {len(subset):5d} {model['thanh_cong']:11d} {model['thanh_cong']/len(subset):8.1%} {subset['so_lan_chay'].astype(int).mean():12.2f} {model['cps']:8,.0f} {model['cps']/BASELINE:8.2f}x")

    # A4 · Phí cố định trong phạm vi nội địa + hàng nặng.
    scope = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    scope_model = mo_hinh(runs, scope)
    for volume in (45000, 22500):
        # 45.000 là tổng yêu cầu công ty; chỉ một phần thuộc scope. Dùng
        # tỷ lệ thành công trong scope trên toàn mẫu để giữ đúng quy mô.
        successes_month = volume * scope_model['thanh_cong'] / len(reqs)
        fixed_per_success = 40_000_000 / successes_month
        variable_cps = scope_model['tong'] / scope_model['thanh_cong']
        print(f"A4 · {volume:,} yc/tháng: {successes_month:,.0f} việc thành công; cố định {fixed_per_success:,.0f} đ/việc; tổng {variable_cps + fixed_per_success:,.0f} đ ({(variable_cps + fixed_per_success)/BASELINE:.2f}x)")

    # B1 · Độ nhạy từng yếu tố và giới hạn số lần chạy.
    print('\nB1 · Độ nhạy (so với A2)')
    scenarios = [
        ('Giá token gấp đôi', dict(gia_vao=52, gia_ra=260)),
        ('Giá token giảm một nửa', dict(gia_vao=13, gia_ra=65)),
        ('Xem lại gấp đôi', dict(he_so_xem_lai=2)),
        ('Xem lại giảm một nửa', dict(he_so_xem_lai=0.5)),
        ('Làm lại gấp đôi', dict(he_so_lam_lai=2)),
        ('Làm lại giảm một nửa', dict(he_so_lam_lai=0.5)),
        ('Lương tăng 25%', dict(luong_phut=2500)),
        ('Tối đa 2 lần chạy', dict(max_lan_chay=2)),
        ('Chỉ 1 lần chạy', dict(max_lan_chay=1)),
    ]
    for name, kwargs in scenarios:
        result = mo_hinh(runs, reqs, **kwargs)
        print(f"{name:26s} {result['cps']:9,.0f} đ {((result['cps']/ket_qua['cps'])-1)*100:+6.1f}%")
    pair = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)
    print(f"B2 · Token x2 + xem lại x2: {pair['cps']:,.0f} đ ({(pair['cps']/ket_qua['cps']-1)*100:+.1f}%)")
    print('B3 · Giới hạn và chi phí cả hệ thống (bao gồm nhân viên xử lý yêu cầu không thành công):')
    for limit in (1, 2, 3):
        result = mo_hinh(runs, reqs, max_lan_chay=limit)
        failed = len(reqs) - result['thanh_cong']
        system_cost = result['tong'] + failed * BASELINE
        print(f"  {limit} lần: agent {result['tong']:,.0f} đ; lỗi {failed}; cả hệ thống {system_cost:,.0f} đ; CPS {result['cps']:,.0f} đ")
    # B4 · Xem lại toàn bộ yêu cầu phạm vi pilot (5 phút/ca xem lại,
    # 9 phút/ca làm lại theo giả định hướng dẫn) và đối chiếu với phút simulated.
    pilot = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    pilot_ids = set(pilot['request_id'])
    pilot_runs = runs[runs['request_id'].isin(pilot_ids)]
    ok_ids = set(pilot_runs.loc[pilot_runs['status'] == 'ok', 'request_id'])
    n_rework = int((pilot['ket_qua'] == 'lam_lai').sum())
    pilot_trace_cost = float((pilot_runs['tokens_in'] / 1000 * GIA_VAO +
                              pilot_runs['tokens_out'] / 1000 * GIA_RA +
                              pilot_runs['tool_calls'] * GIA_TOOL).sum())
    n_success = int((pilot['ket_qua'] == 'thanh_cong').sum())
    review_all_cost = pilot_trace_cost + len(ok_ids) * 5 * LUONG_PHUT + n_rework * 9 * LUONG_PHUT
    review_all_cps = review_all_cost / n_success
    rework_rows = pilot[pilot['ket_qua'] == 'lam_lai']
    all_rework_rows = reqs[reqs['ket_qua'] == 'lam_lai']
    avg_rework_minutes = all_rework_rows['phut_lam_lai_simulated'].astype(float).mean() if len(all_rework_rows) else 0.0
    simulated_review_all_cost = pilot_trace_cost + len(ok_ids) * 5 * LUONG_PHUT + n_rework * avg_rework_minutes * LUONG_PHUT
    simulated_review_all_cps = simulated_review_all_cost / n_success
    print(f"B4 · 100% xem lại ({len(ok_ids)} ca × 5 phút, {n_rework} ca làm lại × {avg_rework_minutes:.1f} phút simulated): {review_all_cps:,.0f} đ/việc ({review_all_cps/BASELINE:.2f}x); dùng phút làm lại simulated: {simulated_review_all_cps:,.0f} đ/việc ({simulated_review_all_cps/BASELINE:.2f}x).")
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
