# Báo cáo cá nhân — TranHoangPhat-2A202603536

## 1. Thông tin thành viên

- Họ tên: Trần Hoàng Phát
- MSSV: 2A202603536
- Email: 26ai.phatth@vinuni.edu.vn
- Vai trong nhóm: Người 2 · Pilot & Số liệu (CP4 + Kiểm số)

## 2. Phần việc phụ trách

Tuân thủ đúng phân công cho vị trí **Người 2: Pilot & Số liệu (CP4 + Kiểm số)**:
1. **Kiểm số cho Người 1 (CP1/CP2):** Tính tay và viết script độc lập để kiểm tra chéo 1 con số cốt lõi của CP1/CP2 (chi phí mỗi việc thành công và các cấu phần chi phí) đối chiếu với Người 1; rà soát số liệu trong `report/team/bang_chi_phi.md`.
2. **Nhiệm vụ D (CP4 · Pilot & Số liệu):**
   - Code độc lập phần D1 (5 câu cỡ mẫu bằng `statsmodels` và công thức giải tích) và đo tỉ lệ `mo_lai_trong_7_ngay` từ `src/logix_requests.csv`.
   - Trả lời đầy đủ D2 (5 câu kiểm tra tách tác động).
   - Điền toàn bộ các trường và $\ge 3$ luật dừng chuẩn cú pháp (NẾU – TRONG – THÌ – KHÔNG THÌ) vào `report/team/pilot_plan.yaml`.
   - Ghép code D1 vào vị trí `TODO CP4` trong `src/lab13.py`.
   - Chạy kiểm tra tự động `yaml.safe_load` và quét `grep '?'` đảm bảo không còn trường trống.
3. **Sản phẩm bàn giao:**
   - `report/team/pilot_plan.yaml`
   - `src/lab13.py` (khối CP4)

## 3. Đóng góp cụ thể

- **Tính tay kiểm tra chéo số liệu CP1/CP2 cho Người 1:**
  - Tính toán độc lập các thành phần chi phí từ 1.624 lần chạy và 1.200 yêu cầu: token = 245.585 đ, tool = 84.000 đ, xem lại = 1.780.000 đ [simulated], làm lại = 2.264.000 đ [simulated], tổng = 4.373.585 đ cho 978 yêu cầu thành công.
  - Con số chốt kiểm tra chéo: Chi phí mỗi việc thành công (**CPS**) = **4.472 đ [simulated]**, khớp chính xác 100% với hàm `mo_hinh()` của Người 1 và đáp án chuẩn. Đồng thời xác minh 3 phép thử A1 (1,20 · 1,25 · 1,25) và điểm hoà vốn xem lại 100%.
- **Code độc lập phần D1 (5 câu cỡ mẫu bằng statsmodels & NormalDist):**
  - *Câu a (chia theo yêu cầu, +5 điểm):* 1.250 yêu cầu mỗi nhóm (công thức giải tích ra 1.251).
  - *Câu b (chia theo nhân viên, m = 75):* Hệ số thiết kế $DE = 1 + (75 - 1) \times 0{,}02 = 2{,}48$; nhân lên thành 3.100 yêu cầu mỗi nhóm $\rightarrow$ cần 42 nhân viên/nhóm (tổng 84 nhân viên $> 40$ nhân viên hiện có $\rightarrow$ không đủ người).
  - *Câu c (20 nhân viên mỗi nhóm):* Cỡ mẫu hiệu dụng tối đa $c / ICC = 20 / 0{,}02 = 1.000 < 1.250 \rightarrow$ không đạt mục tiêu 5 điểm.
  - *Câu d (6 depot mỗi nhóm):* Cỡ mẫu hiệu dụng tối đa $6 / 0{,}02 = 300 < 1.250 \rightarrow$ không đạt và vi phạm điều kiện $\ge 20$ cụm.
  - *Câu e (chấp nhận mức chênh 6 điểm, 20 nhân viên mỗi nhóm):* Cần 858 yêu cầu/nhóm (giải tích ra 859); giải điều kiện cụm ra $m \ge 297$ yêu cầu/nhân viên (giải tích ra 299) với $DE = 6{,}92$.
  - *Phân tích đánh đổi:* Lượng hóa rõ nếu tác động thật là 5 điểm thì tại cỡ mẫu 859, statistical power giảm từ 80% xuống còn **64,12%** (nguy cơ bỏ sót tác động thật là ~36%).
- **Đo tỉ lệ `mo_lai_trong_7_ngay` từ `logix_requests.csv`:**
  - Toàn mẫu: $51 / 1.200 = 4{,}25\%$; phạm vi `noi_dia` + `hang_nang`: $39 / 982 = 3{,}97\%$ [simulated].
  - Bác bỏ đề xuất ngưỡng dừng tuyệt đối 3% (sẽ dừng nhầm pilot ngay tuần đầu do baseline đã là 3,97%), xây dựng ngưỡng an toàn tương đối: chênh lệch $\ge +2$ điểm phần trăm so với đối chứng, kèm trần tuyệt đối 6%.
- **Trả lời D2 (5 câu tách tác động):**
  - Ghi nhận chi tiết trong phần chú thích đầu file `pilot_plan.yaml`: (1) đối chứng song song 20 NV cùng tuần/depot; (2) bốc thăm phân tầng bằng seed ghi trước; (3) nguy cơ tràn tác động và biện pháp kiểm soát bằng tài khoản riêng và log staff_id; (4) chỉ số/ngưỡng/ngày chốt trước ngày chạy; (5) bảo đảm đủ đúng 20 cụm mỗi nhóm.
- **Điền toàn bộ các trường và 3 luật dừng vào `pilot_plan.yaml`:**
  - Điền đầy đủ: owner ("Giám đốc vận hành LogiX-VN"), scope (`noi_dia` + `hang_nang`), rollout `[0.10, 0.25, 0.50]`, primary metric (MDE 0,06, power 0,80, n=859), identifiability, rollback (30 phút, chuyển sang luồng thủ công 12.000 đ), simulated inputs.
  - 3 luật dừng chuẩn cú pháp 4 vế NẾU – TRONG – THÌ – KHÔNG THÌ:
    1. An toàn: NẾU tỉ lệ mở lại 7 ngày cao hơn đối chứng $\ge 2$ điểm hoặc vượt 6% TRONG 3 ngày liên tiếp THÌ Giám đốc vận hành tắt trợ lý trong 30 phút và quay về luồng thủ công KHÔNG THÌ không được sang bước rollout tiếp theo.
    2. Chi phí: NẾU chi phí mỗi việc thành công $> 8.000$ đ [simulated] TRONG 2 tuần liên tiếp THÌ PM thu hẹp về `noi_dia` và giới hạn 2 lần chạy KHÔNG THÌ không được mở rộng sang `hang_nang`.
    3. Sử dụng: NẾU tỉ lệ nhân viên bỏ qua gợi ý $> 40\%$ TRONG 1 tuần THÌ Trưởng nhóm CSKH phỏng vấn 5 nhân viên trong 3 ngày KHÔNG THÌ không được chuyển bước rollout tiếp theo.
- **Ghép code D1 vào `src/lab13.py` và kiểm thử:**
  - Ghép hoàn thiện các hàm D1 (`co_mau_hai_ti_le`, `in_nhiem_vu_d_e`), chạy toàn bộ file `lab13.py` thông suốt từ đầu đến cuối đạt 100%.

## 4. Bằng chứng

- **Lịch sử Commit:**
  - Commit `effe33d`: *"Complete CP4: sample size analysis (D1), impact separation (D2), and pilot_plan.yaml"* do tài khoản `phattoohig` commit và push trực tiếp lên nhánh `main`.
  - Commit `79b42bef`: Hợp nhất toàn bộ nhiệm vụ nhóm A–E trên `main`, giữ nguyên code CP4 và file `pilot_plan.yaml`.
- **Sản phẩm code:** [src/lab13.py](file:///Users/phat/K5-L3A-DAY13-XYZ-LaunchEconomics/src/lab13.py) tích hợp khối D1/CP4, chạy tự động in đầy đủ 5 câu cỡ mẫu, tỉ lệ mở lại và kiểm tra chéo chi phí.
- **Sản phẩm kế hoạch pilot:** [report/team/pilot_plan.yaml](file:///Users/phat/K5-L3A-DAY13-XYZ-LaunchEconomics/report/team/pilot_plan.yaml) pass kiểm tra `yaml.safe_load`, `grep -c '?'` trả về đúng `0` ngoài chú thích.
- **Bảng chi phí kiểm chéo:** [report/team/bang_chi_phi.md](file:///Users/phat/K5-L3A-DAY13-XYZ-LaunchEconomics/report/team/bang_chi_phi.md) khớp chính xác con số tính tay CPS 4.472 đ [simulated].

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity AI Assistant.
- **Mục đích sử dụng:**
  - Hỗ trợ tra cứu nhanh API `NormalIndPower().solve_power` và `proportion_effectsize` trong gói `statsmodels.stats`.
  - Hỗ trợ format cú pháp cấu trúc file YAML đảm bảo không lỗi indentation.

## 6. Tự đánh giá

- Hoàn thành đầy đủ 100% tất cả các đầu việc được giao của **Người 2** theo đúng tiến độ và tiêu chuẩn bài lab.
- Phối hợp đồng bộ và hỗ trợ tốt cho Người 1 (kiểm tra chéo chi phí) và Người giữ hồ sơ (cung cấp dữ liệu pilot cho hồ sơ tổng hợp).
- Báo cáo trung thực, số liệu nhất quán giữa code, YAML và bảng markdown, đáp ứng toàn diện rubric đánh giá 100 điểm.
