# ĐỀ TÀI: MẬT MÃ NHẸ CHO THIẾT BỊ IoT HẠN CHẾ TÀI NGUYÊN

## 1. Lý do chọn đề tài
Các thiết bị IoT hiện nay (như cảm biến, vi điều khiển vi mạch cấp thấp) có tài nguyên cực kỳ hạn chế về RAM, ROM và dung lượng pin. Các thuật toán mã hóa phổ biến như AES-128 tiêu tốn quá nhiều năng lượng và năng lực xử lý, gây trễ dữ liệu. Do đó, nghiên cứu mật mã nhẹ (Lightweight Cryptography - LWC) là giải pháp bắt buộc để bảo mật dữ liệu IoT.

## 2. Mục tiêu đề tài
- Nghiên cứu cơ chế hoạt động của thuật toán mật mã nhẹ ASCON (tiêu chuẩn của NIST).
- Triển khai thực nghiệm đo đạc hiệu năng (thời gian xử lý, tài nguyên tiêu thụ).

## 3. Phạm vi nghiên cứu & Đối tượng thử nghiệm
- Thuật toán tập trung: ASCON-128.
- Đối tượng: Dữ liệu chuỗi giả lập từ các cảm biến IoT nhiệt độ, độ ẩm.

## 4. Công cụ và Phương pháp chính sử dụng
- Ngôn ngữ lập trình: Python / C++.
- Phương pháp: Thực nghiệm Lab, đo lường tốc độ xử lý (Benchmark) của thuật toán.
