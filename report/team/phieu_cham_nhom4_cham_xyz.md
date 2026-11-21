# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Nhóm 4
- Nhóm được chấm: Nhóm XYZ


| Tiêu chí | Điểm | Lý do (có số) |
| --- | ---: | --- |
| Đề xuất khớp bằng chứng | 10/10 | Đề xuất Go có điều kiện nêu rủi ro xem lại 100% làm chi phí đạt 0,98–1,03× và power khoảng 0,64 nếu tác động thật là 5 điểm; nhóm đưa ra điều kiện xử lý. |
| Số giả lập và phạm vi | 10/10 | Các khoản chi phí được ghi simulated; phạm vi pilot giới hạn ở noi_dia và hang_nang. Nhóm loại quoc_te với chi phí 1,88× mức nhân viên tự làm (simulated). |
| Pilot ra được quyết định | 10/10 | Hồ sơ nêu chia ngẫu nhiên 20 + 20 nhân viên, cần 299 yêu cầu/người, đạt khoảng 859 mẫu hiệu dụng/nhóm và có 3 luật dừng. |
| **Tổng** | **30/30** | Chấm dựa trên trang hồ sơ launch v0 đã nhận. |

**Quyết định của hội đồng:** Go có điều kiện.

**Lý do:** Nhóm XYZ trình bày đề xuất Go có điều kiện phù hợp với số liệu, ghi nhãn simulated cho các kết quả chi phí và giới hạn pilot ở noi_dia và hang_nang. Hồ sơ nêu phương án chia ngẫu nhiên 20 + 20 nhân viên, cỡ mẫu và đánh đổi khi chọn MDE 6 điểm. Nhóm cũng chỉ ra rủi ro chi phí khi xem lại 100%, power giảm nếu tác động thật là 5 điểm, cùng các điều kiện xử lý có người phụ trách và hạn kiểm tra.

**Một câu hỏi cho đội trình:** Khi phải xem lại 100%, chi phí có thể lên 12.415 đ/việc (simulated), cao hơn mức 12.000 đ nhân viên tự làm. Nhóm dựa vào điều kiện nào để giảm tỉ lệ xem lại mà vẫn bảo đảm an toàn?

**Câu trả lời của đội trình (ghi lại tại buổi):** Để giảm tỉ lệ xem lại từ 100% xuống dưới 50% (ở cuối bước 0.25) và tiến tới < 30% mà vẫn bảo đảm an toàn, nhóm dựa trên 3 điều kiện đo được đã ghi trong chi_so.md và pilot_plan.yaml:
Điều kiện mở bậc giảm xem lại: Chỉ giảm xem lại ở các loại ổn định (ưu tiên noi_dia đang đạt 95,0% thành công) khi tỉ lệ bỏ qua gợi ý (sua + bo) giảm dưới 15% (so với 27,12% lúc chạy thử) và tỉ lệ mở lại 7 ngày < 4% (thấp hơn nền 3,97% trong phạm vi), đồng thời kiểm soát thời gian xem lại thật ≤ 5 phút để dưới mức hoà vốn 4,8–5,1 phút.
Khoá lỗi nghiêm trọng trước khi giảm xem lại: Đã hoàn tất sửa khoá chống trùng (idempotency_key) và job đối soát sổ cái mỗi giờ (ngưỡng 0 ca, ca 7 & ca 20) trước khi mở pilot.
Hàng rào an toàn chạy song song: Khi giảm xem lại, vẫn chạy kiểm tra mẫu ngẫu nhiên 100 đơn/tuần (audit_sample_checked) để bắt lỗi ngầm, và giữ nguyên luật dừng cứng (nếu mở lại 7 ngày cao hơn đối chứng ≥ +2 điểm %, hoặc vượt trần 6%, hoặc có ≥ 1 ca hoàn trùng trong 3 ngày liên tiếp thì Giám đốc vận hành tắt trợ lý trong 30 phút).