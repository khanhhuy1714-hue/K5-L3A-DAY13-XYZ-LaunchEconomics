# Báo cáo cá nhân — PhamHongKhanhHuy-2A202603588

## 1. Thông tin thành viên

- Họ tên: Phạm Hồng Khánh Huy
- MSSV: 2A202603588
- Email: 26ai.huyphk@vinuni.edu.vn
- Vai trong nhóm: Người gắn nhãn 1 (kiêm đặc tả chỉ số, event, rủi ro kinh tế và kiểm tra chất lượng hồ sơ)

## 2. Phần việc phụ trách

- Thực hiện Nhiệm vụ C (CP3): gắn nhãn độc lập 20 ca lỗi theo khung Google PAIR, đối chiếu đồng thuận với Người gắn nhãn 2, viết quy tắc cho ca lệch và xây dựng bảng khắc phục 5 ca.
- Thực hiện Nhiệm vụ E1, E2 (CP5): tính thử 3 chỉ số trên `1.200` yêu cầu, đề xuất 2 chỉ số mới, thiết kế danh sách event có `trace_id`, kiểm tra chéo công thức tính và lập bảng rủi ro kinh tế trong `report/team/chi_so.md`.
- Rà soát tuân thủ quy tắc toàn bộ bộ hồ sơ (nhãn `simulated`, người phụ trách là một vai trò cụ thể, không dùng từ cấm, kiểm tra đầu ra thực tế từ `src/lab13.py` và `yaml.safe_load`).

## 3. Đóng góp cụ thể

- Hoàn thành bảng gắn nhãn 20 ca và thống nhất nhãn chuẩn với tỉ lệ đồng thuận `17/20 = 85%`, lập 3 quy tắc phân biệt (ca 9, ca 12, ca 18) và 5 giải pháp khắc phục đo được theo ngưỡng và vai trò phụ trách trong `report/team/bang_loi.md`.
- Xác định đầy đủ `10` event gắn `trace_id` bảo đảm đo được toàn bộ `5` chỉ số (bao gồm thay thế hai cột `_simulated` bằng thời gian đo thật ở `staff_review_decision` và `staff_rework_completed`).
- Liên kết trực tiếp các kết quả độ nhạy (`+51,8%` làm lại ×2; `0,98×–1,03×` khi xem lại 100%; `+2.370 đ` cố định ở nửa khối lượng) thành 3 dòng rủi ro kinh tế có ngưỡng theo dõi và hành động trong `report/team/chi_so.md`.

## 4. Bằng chứng

- File [report/team/bang_loi.md](bang_loi.md): 20 ca lỗi (đồng thuận `85%`), 3 quy tắc phân biệt và bảng khắc phục 5 loại.
- File [report/team/chi_so.md](chi_so.md): 5 chỉ số (3 chỉ số tính thử đúng `82,83%`, `27,12%`, `4,25%`), 10 event có `trace_id` và 3 rủi ro kinh tế.
- Kiểm tra chéo file [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md) và [report/team/pilot_plan.yaml](pilot_plan.yaml) khớp số chạy từ `src/lab13.py`.

## 5. Công cụ AI đã dùng

- Sử dụng trợ lý AI để hỗ trợ tổng hợp cấu trúc báo cáo, gợi ý cài đặt Python (`src/lab13.py`), đề xuất bảng khắc phục lỗi và kiểm tra chéo tính nhất quán của toàn bộ tài liệu.
- Tự kiểm tra kết quả bằng cách chạy trực tiếp `src/lab13.py` trên dữ liệu thật (`logix_runs.csv`, `logix_requests.csv`), đối chiếu toàn bộ số với tài liệu hướng dẫn (`docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`), chạy kiểm tra `yaml.safe_load` cho `pilot_plan.yaml` và quét từ khoá vi phạm quy tắc trên toàn bộ thư mục `report/team/`.

## 6. Tự đánh giá

- Hoàn thành đầy đủ phần việc được giao đúng tiến độ, số liệu thống nhất giữa code và toàn bộ hồ sơ nhóm, tuân thủ đầy đủ rubric 100 điểm của lab.
