# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phạm Hồng Khánh Huy · Người gắn nhãn 2: Nguyễn Quốc Việt (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Hệ thống | Không | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Hệ thống | Không | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 17 / 20 = 85%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 9 (Do người dùng):** Gắn nhãn theo nguyên nhân gốc là khách nhập sai mã (mã sàn thương mại điện tử thay vì mã vận đơn); việc trợ lý chưa gợi ý cách sửa nằm ở cột khắc phục chứ không biến lỗi thành lỗi Hệ thống.
- **Ca 12 (Ngầm):** Sai có thể là sai về chi phí chứ không chỉ sai kết quả trả lời — việc token của depot D05 tăng gấp 3 lần suốt 3 tuần mà không cảnh báo hay ai phát hiện thuộc loại Ngầm thay vì Hệ thống.
- **Ca 18 (Ngữ cảnh):** Số tiền 15.000 đ hoàn toàn đúng chính sách và thiết kế, chỉ có giả định "khách tự hiểu cách tính 50%" không khớp với kỳ vọng thực tế của khách, nên thuộc Ngữ cảnh.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (loại `ma_khong_hop_le`); cảnh báo khi > 2% tổng số yêu cầu/ngày | Tự nhận diện định dạng mã sàn TMĐT để tra sang mã vận đơn; nếu không tra được thì hiện hướng dẫn lấy mã vận đơn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Job đối soát mỗi giờ: đếm thông báo "đã hoàn" không có event `refund_ledger_write` `status=ok` cùng `trace_id`; ngưỡng 0 ca | Chỉ gửi thông báo "đã hoàn" sau khi nhận `ok` từ sổ cái (kèm `idempotency_key`); lỗi 503 sau 3 lần thì báo "đang xử lý" và phát `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` có lý do `khieu_nai_so_tien` nhưng kiểm tra lại thấy số tiền đúng, theo dõi hàng tuần; ngưỡng > 1% số đơn đóng | Cập nhật mẫu tin nhắn luôn ghi công thức tính rõ ràng (ví dụ `30.000 đ × 50% = 15.000 đ`) kèm điều khoản áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason=thieu_du_lieu_hang_ngoai`, thống kê theo `loai` mỗi tuần; ngưỡng > 5% trong phạm vi pilot | Giữ luồng chuyển nhân viên kèm tóm tắt đầy đủ thông tin đã thu thập và loại hẳn nhóm `quoc_te` khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu ngẫu nhiên 100 đơn/tuần so với bảng giá hiện hành; ngưỡng ≥ 1% đơn lệch tiền | Tự động xoá bộ nhớ đệm bảng giá ngay khi cập nhật phiên bản mới và ghi `price_table_version` vào mọi `trace_id` | Kế toán trưởng |
