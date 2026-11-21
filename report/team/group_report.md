# Báo cáo nhóm

## 1. Thông tin nhóm

- Tên nhóm: XYZ
- Lớp: L3A
- Thành viên: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Nhóm thực hiện đánh giá kinh tế và thiết kế kế hoạch pilot cho trợ lý hoàn phí của LogiX-VN (Gate 2a) từ dữ liệu giả lập gồm `1.200` yêu cầu và `1.624` lần chạy. Cách tiếp cận kết hợp tính toán mô hình chi phí từ trace (Cost-of-Pass), phân tích độ nhạy, gắn nhãn nguyên nhân gốc theo khung Google PAIR, tính cỡ mẫu cụm bằng `statsmodels` và tổng hợp bộ hồ sơ quyết định một trang.

## 3. Giải pháp

- **Nhiệm vụ A & B (Kinh tế & độ nhạy):** Hoàn thành mã nguồn [src/lab13.py](../../src/lab13.py) (vượt qua cả 3 phép thử A1: `1,20 · 1,25 · 1,25`) và ghi đầy đủ bảng A2–A4, B1–B4 trong [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Phân loại lỗi):** Hai thành viên gắn nhãn độc lập 20 ca lỗi theo 5 loại Google PAIR, đạt đồng thuận `17/20 = 85%`, thống nhất quy tắc phân biệt 3 ca lệch và lập bảng khắc phục 5 loại tại [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính 5 câu D1, kiểm tra 5 điều kiện tách tác động D2 và hoàn thiện [pilot_plan.yaml](pilot_plan.yaml) (chia theo nhân viên `20 + 20`, 3 luật dừng đủ 4 vế).
- **Nhiệm vụ E (Chỉ số & hồ sơ):** Đặc tả 5 chỉ số, 10 event có `trace_id`, 3 rủi ro kinh tế trong [chi_so.md](chi_so.md) và tổng hợp trang quyết định tại [ho_so_launch_v0.md](ho_so_launch_v0.md). Phiếu chấm duyệt chéo [phieu_cham.md](phieu_cham.md) giữ sẵn mẫu để điền trực tiếp khi chấm nhóm `n + 1` lúc 17:00.

## 4. Kết quả

- **Chi phí (simulated):** Chi phí mỗi việc thành công toàn mẫu là `4.472 đ` (`simulated`), gấp `16,3×` hoá đơn token + tool (`274,7 đ`); chi phí cả hệ thống đạt `5.865 đ/yêu cầu = 0,49×` của `12.000 đ` (`simulated`). Trong phạm vi pilot `noi_dia + hang_nang` (đã cộng chi phí cố định `40 triệu đ/tháng`), chi phí là `4.599 đ = 0,38×` ở quy mô `45.000` yêu cầu/tháng (`simulated`).
- **Độ nhạy & giới hạn:** Yếu tố nhạy nhất là số ca làm lại (`+51,8%` khi ×2, `simulated`), kế đến xem lại (`+40,7%`). Giới hạn `2` lần chạy cho tổng chi phí cả hệ thống thấp nhất (`6.901.220 đ`, `simulated`). Nếu xem lại 100%, chi phí vọt lên `11.743 đ = 0,98×` (9 phút làm lại) hoặc `12.415 đ = 1,03×` (15,3 phút, `simulated`).
- **Chỉ số đợt chạy thử (không đối chứng):** Chỉ số chính trong đợt chạy thử là `82,83%`, tỉ lệ bỏ qua gợi ý `27,12%`, tỉ lệ mở lại trong 7 ngày `4,25%` (`3,97%` trong phạm vi).
- **Đề xuất Gate 2a:** **Go có điều kiện** cho pilot phạm vi `noi_dia + hang_nang` (tối đa 2 lần chạy), kèm 4 điều kiện có vai trò phụ trách và hạn kiểm tra rõ ràng. Kết quả duyệt chéo của hội đồng sẽ cập nhật sau phiên 17:00.

## 5. Khó khăn và cách xử lý

- Dữ liệu chạy thử chưa có nhóm đối chứng nên không thể khẳng định mức cải thiện trực tiếp từ 70% lên 82,83%; nhóm xử lý bằng cách chỉ báo cáo trị số đợt chạy thử và thiết kế pilot có đối chứng đồng thời `20 + 20`.
- Số lượng nhân viên hiện có (`40` người) không đủ đạt power `0,80` cho mức chênh `5` điểm khi chia theo cụm; nhóm giải quyết bằng việc tính rõ giới hạn `c / ICC = 1.000`, chọn `MDE = 6 điểm` (`m ≥ 299`, `DE = 6,96`) và công khai đánh đổi `power ≈ 0,64` ở mức 5 điểm.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong [TEAM.md](../../TEAM.md).

## 7. Hạn chế và hướng cải thiện

- Thời gian xem lại và làm lại hiện là dữ liệu `simulated` chiếm tới `92,5%` tổng chi phí; cần bật đủ 10 event có `trace_id` để thay bằng phút đo thật ngay sau tuần 1.
- Nếu tiếp tục xem lại 100%, pilot sẽ mất lợi thế chi phí; cần thực thi lộ trình giảm tỉ lệ xem lại theo bậc dựa trên ngưỡng an toàn và tỉ lệ sửa/bỏ gợi ý.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu `statsmodels`, lớp `NormalIndPower` (`stats.power`)
