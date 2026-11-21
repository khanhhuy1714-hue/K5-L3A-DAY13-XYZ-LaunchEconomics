# Team

## Thông tin nhóm

- Tên nhóm: XYZ
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-XYZ-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/khanhhuy1714-hue/K5-L3A-DAY13-XYZ-LaunchEconomics`, nhánh `main`, commit "finish lab13"

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
| 1 | Trịnh Quốc Đạt | 2A202603581 | 26ai.dattq2@vinuni.edu.vn | https://github.com/Trinh-Quoc-Dat | Người viết code (CP1, CP2) |
| 2 | Trần Hoàng Phát | 2A202603536 | 26ai.phatth@vinuni.edu.vn | https://github.com/phattoohigh | Người kiểm số (nửa đầu), Người viết code 2 (CP4) |
| 3 | Phạm Hồng Khánh Huy | 2A202603588 | 26ai.huyphk@vinuni.edu.vn | https://github.com/khanhhuy1714-hue | Người gắn nhãn 1 (kiêm chỉ số và kiểm tra chất lượng) |
| 4 | Nguyễn Quốc Việt | 2A202603556 | 26ai.vietnq3@vinuni.edu.vn | https://github.com/quocvietnguyen7055 | Người gắn nhãn 2, kiêm giữ hồ sơ (nhóm trưởng, điều phối Gate 2a) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/team/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/2A202603588_PhamHongKhanhHuy.md`.

## Trịnh Quốc Đạt - 2A202603581

### Phần việc phụ trách

- Thiết lập môi trường Python (`src/.venv`) và triển khai phần CP1, CP2 trong `src/lab13.py`.
- Phối hợp cùng người kiểm số hoàn thiện `report/team/bang_chi_phi.md`.

### Đóng góp cụ thể

- Viết ba hàm A1 đạt 100% phép thử đáp án biết trước (`1,20 · 1,25 · 1,25`) và hàm `mo_hinh` cho A2, A3, A4.
- Triển khai các kịch bản phân tích độ nhạy B1, B2, giới hạn chạy lại B3 và phân tích xem lại 100% B4.

### Bằng chứng

- File `src/lab13.py` chạy từ đầu đến cuối in ra đầy đủ bảng A1–A4, B1–B4.
- File `report/team/bang_chi_phi.md`.

## Trần Hoàng Phát - 2A202603536

### Phần việc phụ trách

- Tính tay kiểm chứng số liệu ở CP1–CP2 và điền bảng vào `report/team/bang_chi_phi.md`.
- Đảm nhận vai trò người viết code 2 ở nửa sau: tính cỡ mẫu D1 và hoàn thiện `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Đối chiếu thủ công chi phí mỗi việc thành công (`4.472 đ`, `simulated`), chi phí cố định 40 triệu đ/tháng và điểm hoà vốn xem lại 100%.
- Triển khai phần D1 (5 câu cỡ mẫu với `NormalDist` và `statsmodels`), trả lời 5 câu D2, tính tỉ lệ mở lại nền (`4,25%` toàn bộ; `3,97%` trong phạm vi) và viết 3 luật dừng đủ 4 vế trong `report/team/pilot_plan.yaml`.

### Bằng chứng

- Hàm `co_mau_hai_ti_le` và phần `in_nhiem_vu_d_e` trong `src/lab13.py`.
- File `report/team/pilot_plan.yaml` vượt qua kiểm tra `yaml.safe_load` và không còn dấu `?` ngoài chú thích.

## Phạm Hồng Khánh Huy - 2A202603588

### Phần việc phụ trách

- Người gắn nhãn 1 cho 20 ca lỗi theo khung Google PAIR (CP3).
- Đặc tả chỉ số, danh sách event có `trace_id`, bảng rủi ro kinh tế (CP5) và kiểm tra chất lượng toàn bộ hồ sơ.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi, cùng người gắn nhãn 2 đối chiếu đạt đồng thuận `17/20 = 85%`, xây dựng quy tắc cho 3 ca lệch và bảng khắc phục 5 ca.
- Tính thử 3 chỉ số E1, đề xuất 2 chỉ số mới, thiết kế 10 event có `trace_id`, kiểm tra chéo công thức tính chỉ số và hoàn thiện 3 dòng rủi ro kinh tế trong `report/team/chi_so.md`.
- Rà soát toàn bộ checklist nộp bài (nhãn `simulated`, người phụ trách là một vai trò cụ thể, không dùng từ cấm).

### Bằng chứng

- File `report/team/bang_loi.md`, `report/team/chi_so.md`.
- Báo cáo cá nhân `report/team/2A202603588_PhamHongKhanhHuy.md`.

## Nguyễn Quốc Việt - 2A202603556

### Phần việc phụ trách

- Nhóm trưởng, tạo repo nhóm `K5-L3A-DAY13-XYZ-LaunchEconomics`, cập nhật `TEAM.md`.
- Người gắn nhãn 2 (20 ca lỗi) và người giữ hồ sơ (`report/team/ho_so_launch_v0.md`), điều phối duyệt chéo Gate 2a và tổng hợp `report/team/group_report.md`.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi và phối hợp thống nhất 20/20 ca theo nguyên nhân gốc vào `report/team/bang_loi.md`.
- Tổng hợp 7 mục vào trang hồ sơ `report/team/ho_so_launch_v0.md`, chốt đề xuất `Go có điều kiện` kèm 4 điều kiện cụ thể và viết báo cáo nhóm `report/team/group_report.md`.

### Bằng chứng

- File `TEAM.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`.
