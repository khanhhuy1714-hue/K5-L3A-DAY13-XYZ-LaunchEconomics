# Báo cáo cá nhân — Trịnh Quốc Đạt (2A202603581)

## 1. Thông tin thành viên

- Họ tên: Trịnh Quốc Đạt
- MSSV: 2A202603581
- Email: 26ai.dattq2@vinuni.edu.vn
- Vai trong nhóm: Người viết code (CP1, CP2)

## 2. Phần việc phụ trách

- Hoàn thiện các phép tính kinh tế CP1–CP2 trong `src/lab13.py`.
- Phối hợp điền và đối chiếu `report/team/bang_chi_phi.md`.

## 3. Đóng góp cụ thể

- Cài môi trường ảo cho `src/` và hoàn thiện ba hàm A1; các phép thử biết trước đạt `1,20`, `1,25` và `1,25`.
- Viết `mo_hinh` để tính token, tool, thời gian xem lại, thời gian làm lại và chi phí mỗi việc thành công; chi phí token và tool tính trên mọi lần chạy, kể cả lần lỗi.
- Triển khai A3–A4 theo loại yêu cầu và chi phí cố định; triển khai phân tích độ nhạy B1–B4, gồm giới hạn số lần chạy và kịch bản xem lại 100%.
- Điền kết quả CP1–CP2 vào bảng chi phí, gắn nhãn `simulated` cho các số dựa trên thời gian nhân viên giả lập.

## 4. Bằng chứng

- `src/lab13.py` in kết quả A1–A4 và B1–B4; các số chính gồm CPS toàn mẫu `4.472 đ`, CPS `quoc_te` `22.515 đ`, phương án giới hạn 2 lần có chi phí toàn hệ thống thấp nhất `6.901.220 đ`, và B4 `11.743–12.415 đ` tuỳ giả định thời gian làm lại.
- `report/team/bang_chi_phi.md` có bảng A1–A4, độ nhạy B1–B2, so sánh giới hạn B3 và kịch bản B4.
- Commit phần CP1–CP2: `fd1fbb6`.

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI để hỗ trợ triển khai và rà soát công thức, cấu trúc đầu ra, cũng như điền bảng chi phí.
- Tự kiểm tra bằng cách chạy `python lab13.py` trong môi trường ảo ở `src/`; đối chiếu kết quả với hướng dẫn chi tiết của lab. Sau khi pull cập nhật của nhóm, chạy lại bản mới nhất và xác nhận chương trình in hết các phần A1–E1.

## 6. Tự đánh giá

- Hoàn thành phần code CP1–CP2 và bảng chi phí; đã kiểm tra đầu ra trên dữ liệu CSV của lab. Các thời gian xem lại/làm lại trong dữ liệu là `simulated`, nên cần được thay bằng thời gian đo thực tế khi thiết kế pilot.
