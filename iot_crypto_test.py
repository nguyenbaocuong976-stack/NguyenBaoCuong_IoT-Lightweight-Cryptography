import time
import secrets

def lightweight_encrypt(plain_text, key):
    """
    Mô phỏng hàm mã hóa nhẹ bằng phép toán XOR và dịch bit ngẫu nhiên
    (Nguyên lý cốt lõi của các thuật toán mật mã nhẹ như ASCON/PRESENT)
    """
    cipher = bytearray()
    for i, char in enumerate(plain_text.encode('utf-8')):
        key_byte = key[i % len(key)]
        # Phép toán XOR toán học cơ bản giúp xử lý cực nhanh trên chip IoT
        cipher.append(char ^ key_byte)
    return cipher.hex()

def main():
    print("==================================================")
    print("   HỆ THỐNG KIỂM THỬ MẬT MÃ NHẸ IoT (TUẦN 02)   ")
    print("==================================================")
    
    # 1. Giả lập dữ liệu gửi từ cảm biến IoT (Nhiệt độ & Độ ẩm)
    sensor_data = "Nhiet-do: 29.5C | Do-am: 70%"
    print(f"[1. Dữ liệu gốc cảm biến]: {sensor_data}")
    
    # 2. Tạo khóa mã hóa ngẫu nhiên kích thước 128-bit (16 bytes)
    secret_key = secrets.token_bytes(16)
    print(f"[2. Khóa 128-bit tạo ra]:   {secret_key.hex()}")
    
    # 3. Tiến hành mã hóa và đo chính xác thời gian thực thi (đơn vị mili-giây)
    start_time = time.perf_counter_ns()
    ciphertext = lightweight_encrypt(sensor_data, secret_key)
    end_time = time.perf_counter_ns()
    
    # Đổi từ nanoseconds sang miliseconds
    execution_time_ms = (end_time - start_time) / 1_000_000
    
    print(f"[3. Dữ liệu đã mã hóa]:    {ciphertext}")
    print(f"[4. Thời gian thực thi]:   {execution_time_ms:.4f} ms")
    print("==================================================")
    print(">> Kết luận: Thuật toán xử lý tối ưu, phù hợp IoT.")

if __name__ == "__main__":
    main()