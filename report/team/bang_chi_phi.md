# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | có phần simulated |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,3 lần** (4.472 / 274,7).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại: 51,8%** (2.264.000 / 4.373.585; simulated).

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **quoc_te** không đáng làm: CPS 22.515 đ = **1,88×** nhân viên, chỉ thành công 27,3%. Không: tỉ lệ đúng theo attempt giảm từ 30,0% (lần 1) xuống 11,4% và 2,2% ở lần 2, 3.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? **Không** ở 45.000 yêu cầu/tháng (4.599 đ so với 12.000 đ), nhưng làm chi phí cố định mỗi việc tăng gấp đôi khi khối lượng còn 22.500/tháng (tổng 5.784 đ, vẫn dưới baseline).

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ/việc (+46,3%)**, đúng bằng tổng hai mức tăng riêng do mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1%)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ (thấp nhất) | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **Tối đa 2 lần** rẻ nhất cho công ty (6.901.220 đ); không trùng: CPS thấp nhất là 1 lần (4.111 đ), nhưng đẩy thêm 85 yêu cầu sang nhân viên.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: **11.743 đ = 0,98×** (giả định 5 phút xem lại và 9 phút làm lại mỗi ca; simulated). Dữ liệu simulated hiện ghi trung bình 15,3 phút/làm lại thì CPS thành **12.415 đ = 1,03×**.
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% gần hoà vốn: mức xem lại phải ≤ **5,1 phút** (làm lại 9 phút) hoặc ≤ **4,8 phút** (làm lại 15,3 phút); pilot cần đo thời gian thật và tỉ lệ xem lại an toàn có thể giảm.
