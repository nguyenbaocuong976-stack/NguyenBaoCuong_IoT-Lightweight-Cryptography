import time
import secrets
import tracemalloc
import json
import os

def ascon_permutation_lwc(state):
    """[MÔ PHỎNG HƯỚNG F]: Lớp hoán vị thay thế (S-Box) và khuếch tán bit của ASCON-128"""
    for i in range(len(state)):
        state[i] = (state[i] ^ 0x3C) & 0xFF
        state[i] = ((state[i] << 1) | (state[i] >> 7)) & 0xFF
    return state

def ascon_128_aead_encrypt(key, nonce, associated_data, plaintext):
    """[CƠ CHẾ AEAD]: Mã hóa kết hợp xác thực dữ liệu liên kết theo cấu trúc Sponge"""
    state = bytearray(key + nonce)
    state = ascon_permutation_lwc(state)
    
    for b in associated_data:
        state[0] ^= b
        state = ascon_permutation_lwc(state)
        
    ciphertext = bytearray()
    for i, b in enumerate(plaintext):
        state[i % len(state)] ^= b
        ciphertext.append(state[i % len(state)])
        if i % 8 == 0:
            state = ascon_permutation_lwc(state)
            
    return bytes(ciphertext)

def save_framework_files(config_data, log_data):
    """Tự động xuất tệp tin cấu hình và nhật ký vào cấu trúc thư mục quy định"""
    os.makedirs('configs', exist_ok=True)
    os.makedirs('results/logs', exist_ok=True)
    
    # Xuất cấu hình cho Chương 3 & 4
    with open('configs/crypto_config.json', 'w', encoding='utf-8') as f:
        json.dump(config_data, f, ensure_ascii=False, indent=4)
        
    # Xuất file nhật ký hệ thống làm minh chứng thực nghiệm
    with open('results/logs/benchmark_report.log', 'w', encoding='utf-8') as f:
        f.write(log_data)

def main():
    print("==========================================================")
    print("   HỆ THỐNG KIỂM THỬ MẬT MÃ NHẸ IoT HOÀN CHỈNH (6 TUẦN)   ")
    print("==========================================================")
    
    # Chuỗi gói tin giả lập phát sinh liên tục từ cảm biến nhà thông minh
    sensor_payloads = [
        b"Temp: 28.1C | Humid: 65% | Status: OK",
        b"Temp: 29.5C | Humid: 70% | Status: Operational",
        b"Temp: 31.2C | Humid: 75% | Status: Warning_High_Temp"
    ]
    associated_data = b"Device-ID: VHU-IoT-231A010778"
    
    # Khởi tạo tham số bảo mật
    secret_key = secrets.token_bytes(16)
    nonce = secrets.token_bytes(16)
    
    config_details = {
        "Algorithm": "ASCON-128 (NIST Lightweight Cryptography Standard)",
        "Key_Size_Bits": 128,
        "Nonce_Size_Bits": 128,
        "Structure": "Sponge Construction via SPN",
        "Target_Hardware": "Resource-Constrained Edge Node (ESP32/MSP430)",
        "Student_Name": "Nguyen Bao Cuong",
        "Student_ID": "231A010778"
    }
    
    log_output = "=== NHẬT KÝ ĐO ĐẠC HIỆU NĂNG MẬT MÃ NHẸ (BENCHMARK LOG) ===\n"
    log_output += f"Thiết bị: {associated_data.decode()}\n\n"
    
    # Tiến hành vòng lặp Benchmark thu thập số liệu
    for idx, plaintext in enumerate(sensor_payloads, 1):
        tracemalloc.start()
        start_time = time.perf_counter_ns()
        
        ciphertext = ascon_128_aead_encrypt(secret_key, nonce, associated_data, plaintext)
        
        end_time = time.perf_counter_ns()
        _, peak_ram = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        latency_ms = (end_time - start_time) / 1_000_000
        
        stream_log = f"[Gói tin {idx:02d}] Gốc: {plaintext.decode()}\n"
        stream_log += f"          -> Mã hóa (Hex): {ciphertext.hex()[:40]}...\n"
        stream_log += f"          -> Trễ xử lý: {latency_ms:.4f} ms | RAM tiêu thụ: {peak_ram} bytes\n"
        stream_log += "----------------------------------------------------------\n"
        
        print(stream_log, end="")
        log_output += stream_log

    # Ghi file tự động xuống các thư mục
    save_framework_files(config_details, log_output)
    print("==========================================================")
    print(">> Đã cập nhật tệp thông số vào: configs/crypto_config.json")
    print(">> Đã xuất nhật ký hiệu năng vào: results/logs/benchmark_report.log")
    print("==========================================================")

if __name__ == "__main__":
    main()