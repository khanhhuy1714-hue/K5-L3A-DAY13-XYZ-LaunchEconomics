# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): XYZ (L3A)
- Nhóm được chấm: Nhom4 (L3A)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất Go có điều kiện khớp số liệu (0,49× cả hệ thống), nêu thẳng 2 bất lợi: xem lại 100% tốn 0,98×–1,03× và power còn 0,64 ở mức 5 điểm, kèm 4 điều kiện có vai trò phụ trách và hạn kiểm tra rõ. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Mục 1, 2, 3, 7 đều gắn nhãn `[simulated]` và trạng thái Giả lập; thu hẹp phạm vi về `noi_dia` (0,22×) + `hang_nang` (0,69×), loại `quoc_te` (1,88×) và `doi_tac` (0,85×). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia theo nhân viên 20 + 20 có đối chứng đồng thời, phân tầng theo depot; giải thích rõ MDE 6 điểm (`n = 859/nhóm`, `m ≥ 299`, `DE = 6,96`) và có 3 luật dừng (an toàn, chi phí, mức dùng). |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Mô hình kinh tế ở phạm vi `noi_dia + hang_nang` khả thi (`4.599 đ/việc` có cố định = `0,38×` so với `12.000 đ`, `[simulated]`), thiết kế pilot `20 + 20` tách được tác động và đã nêu đủ các điều kiện bắt buộc trước khi chạy (sửa lỗi ca 7 và 20, ký chấp nhận power `0,64` ở 5 điểm, đo phút thật qua `trace_id`, lộ trình hạ xem lại `≤ 5,1` phút).

**Một câu hỏi cho đội trình:** Với tỉ lệ mở lại trong 7 ngày hiện tại là `4,25%` (`3,97%` trong phạm vi), ngưỡng dừng an toàn trong `pilot_plan.yaml` của nhóm bạn đặt là bao nhiêu phần trăm để pilot không bị dừng oan ngay tuần đầu?

**Câu trả lời của đội trình (ghi lại tại buổi):** Nhóm 4 đặt ngưỡng dừng khi tỉ lệ mở lại trong 7 ngày của nhóm trợ lý cao hơn đối chứng từ 2 điểm phần trăm trở lên hoặc vượt trần 6% trong 3 ngày liên tiếp (xử lý ngay nếu có từ 1 ca hoàn trùng). Vì mức nền chạy thử hiện tại là 4,25% toàn mẫu và 3,97% trong phạm vi (đều dưới 6%), pilot không bị dừng oan ngay tuần đầu như trần 3% nhưng vẫn bắt được nếu nhóm trợ lý kém hơn đối chứng từ 2 điểm phần trăm.
