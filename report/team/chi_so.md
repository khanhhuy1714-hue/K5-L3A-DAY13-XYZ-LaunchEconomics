# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994 / 1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48 / 177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51 / 1.200; trong phạm vi `noi_dia + hang_nang` là 3,97% = 39 / 982) |
| Dùng | Nhóm tự đề xuất: Tỉ lệ mở trợ lý trên nhóm can thiệp | Số yêu cầu thuộc nhóm trợ lý có event `agent_suggestion_shown` chia tổng số yêu cầu giao cho nhóm trợ lý | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu tuần | Số đơn lệch số tiền trong `audit_sample_checked` chia tổng số đơn được kiểm tra mẫu (bắt lỗi ngầm như ca 5, 17) | Không cần tính |

Chỉ số trong đợt chạy thử là **82,83%**, không kết luận trợ lý đã nâng chỉ số vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mười event cốt lõi, mỗi event đều gắn `trace_id` để nối với trace của agent và thay thế hai cột `_simulated` bằng phút đo thật.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `loai`, `so_tien_vnd`, `arm`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `price_table_version`, `trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý của trợ lý hiện lên màn hình |
| `staff_review_decision` | Nhân viên CSKH | `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai_thuc`, `trace_id` | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên CSKH | `staff_id`, `phut_lam_lai_thuc`, `ly_do`, `trace_id` | Khi nhân viên hoàn tất làm lại ca sai |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `status`, `trace_id` | Khi ghi bút toán hoàn tiền |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `loai`, `trace_id` | Khi quá số lần chạy hoặc ngoài phạm vi |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `dong_trong_24h`, `trace_id` | Khi yêu cầu chuyển trạng thái đóng |
| `ticket_reopened` | Khách hàng | `request_id`, `reopened_at`, `reason`, `mo_lai_trong_7_ngay`, `trace_id` | Khi khách mở lại yêu cầu trong 7 ngày |
| `audit_sample_checked` | Kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `lech_vnd`, `trace_id` | Kiểm tra mẫu 100 đơn mỗi tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Mọi chỉ số ở bảng trên đều đo được trực tiếp từ danh sách event:

- **Chỉ số chính (% đóng 24h & không mở lại 7 ngày):** ghép `refund_request_created` + `ticket_closed` (điều kiện trong 24h) trừ các `trace_id` xuất hiện trong `ticket_reopened` trong vòng 7 ngày.
- **Tỉ lệ bỏ qua gợi ý:** đếm `staff_review_decision` có `quyet_dinh` thuộc `sua` hoặc `bo` chia cho tổng số `staff_review_decision`.
- **Tỉ lệ lỗi lọt đến khách:** đếm `ticket_reopened` (trong 7 ngày) chia cho tổng số `refund_request_created`.
- **Tỉ lệ mở trợ lý trên nhóm can thiệp:** đếm `agent_suggestion_shown` chia tổng số `refund_request_created` có `arm = treatment`.
- **Tỉ lệ đơn hoàn sai tiền (bắt lỗi ngầm):** đếm `audit_sample_checked` có `lech_vnd != 0` chia tổng số `audit_sample_checked`.

## E2 · Rủi ro kinh tế

Các con số lấy trực tiếp từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng `+51,8%`, từ `4.472 đ` lên `6.787 đ` (`simulated`) | Tỉ lệ `lam_lai` hàng tuần vượt `7%` (mốc chạy thử trong phạm vi là `4,9%` = 48/982) | Thu hẹp phạm vi về chỉ `noi_dia`, rà 20 trace `lam_lai` và giới hạn tối đa 2 lần chạy | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài quá lâu | Chi phí chạm `11.743 đ = 0,98×` (9 phút làm lại) hoặc `12.415 đ = 1,03×` (15,3 phút như dữ liệu), mất lợi thế kinh tế (`simulated`) | Tỉ lệ được xem lại vẫn `> 50%` hoặc `phut_xem_lai_thuc > 5 phút` ở cuối tuần 2 (bước 0.25) | Áp dụng quy trình giảm xem lại theo bậc xuống `< 30%` khi tỉ lệ `sua + bo < 15%` và mở lại `< 4%` | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thực tế thấp hơn kế hoạch | Chi phí cố định `40 triệu đ/tháng` đội từ `+1.185 đ/việc` (45.000 yc/tháng) lên `+2.370 đ/việc` nếu còn một nửa, đẩy tổng từ `4.599 đ` lên `5.784 đ` (`simulated`) | Số việc thành công hàng tuần `< 50%` kế hoạch trong 2 tuần liên tiếp | Tạm dừng mở rộng quy mô pilot và đàm phán lại cấu trúc chi phí cố định hạ tầng | PM trợ lý hoàn phí |
