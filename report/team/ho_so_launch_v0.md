# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức.

Nhóm: XYZ · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu `4.472 đ` (gấp `16,3×` hoá đơn `274,7 đ`); phạm vi `noi_dia + hang_nang`: `3.414 đ` biến đổi, `+1.185 đ` cố định = `4.599 đ` ở 45.000 yc/tháng (`5.784 đ` ở nửa khối lượng) — **simulated** | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (`+51,8%` khi ×2) · 2. Tỉ lệ xem lại (`+40,7%` khi ×2) · 3. Lương nhân viên (`+23,1%` khi +25%); giá token ×2 chỉ `+5,6%` — **simulated** | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống (gồm 222 ca không thành công): `5.865 đ/yêu cầu = 0,49×` của `12.000 đ`; phạm vi pilot + cố định: `0,38×` (`0,48×` ở nửa khối lượng); cảnh báo xem lại 100%: `0,98×–1,03×` — **simulated** | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (chưa có đối chứng): chỉ số chính `82,83%`, bỏ qua gợi ý `27,12%`, mở lại 7 ngày `4,25%` (`3,97%` trong phạm vi); đủ 10 event có `trace_id` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận gắn nhãn độc lập `17/20 = 85%`, thống nhất 20/20 ca theo 5 loại Google PAIR; đủ 5 phương án phát hiện đo được và khắc phục (nổi bật ca 7, 20) | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên `20 + 20`, phạm vi `noi_dia + hang_nang` (tối đa 2 lần chạy), `MDE = 6 điểm` (`n = 859/nhóm`, `DE = 6,96`, `m ≥ 299`; đánh đổi `power = 0,64` ở mức 5 điểm), 3 luật dừng đủ 4 vế, ngày quyết định `2027-01-05` | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | 3 rủi ro chính: làm lại ×2 (`6.787 đ`, `+51,8%`), xem lại 100% (`11.743–12.415 đ`, `0,98×–1,03×`), khối lượng giảm một nửa (`+2.370 đ` cố định/việc) — **simulated** | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** (chỉ duyệt triển khai pilot cho phạm vi `noi_dia` + `hang_nang` với giới hạn tối đa 2 lần chạy; loại `quoc_te` vì `1,88×` và `doi_tac` vì `0,85×` có điều khoản riêng). Bốn điều kiện bắt buộc:

- **Điều kiện 1 (An toàn hệ thống):** Hoàn tất sửa lỗi khoá chống trùng (`idempotency_key`) và job đối soát sổ cái mỗi giờ cho ca 7, ca 20 trước khi mở pilot — **Phụ trách:** Kỹ sư trưởng agent — **Ngày kiểm tra:** `2026-11-27`.
- **Điều kiện 2 (Đánh đổi thống kê):** Ký duyệt chấp nhận `MDE = 6 điểm` (`m ≥ 299` yêu cầu/nhân viên) cùng rủi ro `power ≈ 0,64` nếu tác động thật chỉ đạt 5 điểm — **Phụ trách:** Giám đốc vận hành LogiX-VN — **Ngày kiểm tra:** `2026-11-27`.
- **Điều kiện 3 (Đo lường thật thay số giả lập):** Bật đủ 10 event có `trace_id` và thay toàn bộ phút `simulated` bằng thời gian xem lại/làm lại đo thật ngay sau tuần 1 rollout (`0.10`) — **Phụ trách:** Kỹ sư trưởng agent — **Ngày kiểm tra:** `2026-12-07`.
- **Điều kiện 4 (Lộ trình giảm xem lại):** Ban hành quy tắc hạ tỉ lệ xem lại theo bậc xuống `< 50%` ở cuối bước `0.25`, vì giữ xem lại 100% khiến chi phí lên `0,98×–1,03×` và triệt tiêu lợi ích kinh tế — **Phụ trách:** Trưởng nhóm CSKH — **Ngày kiểm tra:** `2026-12-14`.
