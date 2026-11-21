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
| Tool | 84.000 | `logix_runs.csv` (5.600 lần gọi) | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút) | simulated |
| Tổng chi phí | 4.373.585 | Tổng 4 khoản trên | có phần simulated |
| Số việc thành công | 978 | `ket_qua == 'thanh_cong'` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | `4.373.585 ÷ 978` | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | `(245.585 + 84.000) ÷ 1.200` | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Chi phí mỗi việc thành công (`4.472 đ`, simulated) gấp **16,3 lần** hoá đơn chia số yêu cầu (`274,7 đ`). Nếu cộng thêm `222` ca không thành công để nhân viên tự làm (`12.000 đ/ca`), chi phí cả hệ thống đạt `5.865 đ/yêu cầu = 0,49×` của `12.000 đ` (`simulated`).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? Khoản lớn nhất là **làm lại với 51,8%** (`2.264.000 đ`, simulated), tiếp theo là **xem lại 40,7%** (`1.780.000 đ`, simulated); tổng giờ nhân viên chiếm tới **92,5%** chi phí.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ (simulated) | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ (simulated) | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ (simulated) | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ (simulated) | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? Loại `quoc_te` không đáng chạy vì chi phí đạt `22.515 đ = 1,88×` (`simulated`) với tỉ lệ thành công chỉ `27,3%`. Chạy lại 3 lần không giúp vì tỉ lệ `ok` rớt từ `30,0%` (lần 1) xuống `11,4%` (lần 2) và `2,2%` (lần 3); `doi_tac` (`0,85×`, có điều khoản riêng) cũng được loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (simulated) | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ (simulated) | 0,38× |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370 đ | 5.784 đ (simulated) | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Chi phí cố định `40 triệu đ/tháng` không đổi kết luận ở quy mô đầy đủ (`4.599 đ = 0,38×`) hay nửa khối lượng (`5.784 đ = 0,48×`, simulated; biến đổi phạm vi `3.414 đ`). Tuy nhiên nếu xuống dưới ~`4.659` việc thành công/tháng (~`6.212` yêu cầu/tháng), chi phí cố định vượt `8.586 đ/việc` khiến tổng vượt mốc `12.000 đ`.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ (simulated) | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ (simulated) | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ (simulated) | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ (simulated) | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ (simulated) | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ (simulated) | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ (simulated) | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ (simulated) | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ (simulated) | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%, simulated)**, đúng bằng tổng hai tác động riêng (`+5,6% + 40,7%`) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại (+51,8%)** · 2. **Tỉ lệ xem lại (+40,7%)** · 3. **Lương nhân viên (+23,1%)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ (simulated) | 319 | 7.449.781 đ (simulated) | 4.111 đ (simulated) |
| 2 lần | 4.093.220 đ (simulated) | 234 | 6.901.220 đ (simulated) | 4.237 đ (simulated) |
| 3 lần | 4.373.585 đ (simulated) | 222 | 7.037.585 đ (simulated) | 4.472 đ (simulated) |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Giới hạn **2 lần** rẻ nhất cho công ty (`6.901.220 đ`, simulated), không trùng với mức cho chi phí mỗi việc thành công thấp nhất là **1 lần** (`4.111 đ`, simulated). Ép về 1 lần đẩy thêm `85` ca (`319 − 234`) cho nhân viên tự làm với giá `12.000 đ/ca`, làm chi phí hệ thống tăng `548.561 đ`.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: Với 9 phút làm lại/ca, chi phí là **11.743 đ = 0,98×** của `12.000 đ` (`simulated`, hoà vốn `≤ 5,12` phút xem lại); nếu thay bằng trung bình thực trong dữ liệu là `15,3` phút/ca, chi phí lên **12.415 đ = 1,03×** (`simulated`, đắt hơn nhân viên tự làm, hoà vốn `≤ 4,80` phút).
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% làm tiền xem lại chiếm ~`90%` tổng chi phí và xoá sạch lợi thế kinh tế. Do đó pilot phải đo được thời gian xem lại thật dưới `5` phút và tìm ra ngưỡng tỉ lệ xem lại giảm an toàn theo bậc (dưới `50%`) mà không tăng lỗi lọt khách.
