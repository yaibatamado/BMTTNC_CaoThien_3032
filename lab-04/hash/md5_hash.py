# Bảng hằng số K
k = [
    0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
    0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
    0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
    0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
    0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
    0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
    0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
    0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
    0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
    0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
    0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
    0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
    0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
    0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
    0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
    0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
]

# Bảng hằng số dịch chuyển vòng (rotate shifts)
s = [
    7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
    5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
    4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
    6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21
]

def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(message_bytes):
    # Khởi tạo các biến ban đầu
    a0 = 0x67452301
    b0 = 0xEFCDAB89
    c0 = 0x98BADCFE
    d0 = 0x10325476

    # Tiền xử lý chuỗi văn bản
    original_length_in_bytes = len(message_bytes)
    message_bytes += b'\x80'
    while len(message_bytes) % 64 != 56:
        message_bytes += b'\x00'
    
    # === DÒNG CODE ĐÃ SỬA LỖI ===
    original_length_in_bits = original_length_in_bytes * 8
    message_bytes += original_length_in_bits.to_bytes(8, 'little')
    # ============================

    # Xử lý từng khối 512-bit (64-byte)
    for i in range(0, len(message_bytes), 64):
        block = message_bytes[i:i+64]
        words = [int.from_bytes(block[j:j+4], 'little') for j in range(0, 64, 4)]
        
        a, b, c, d = a0, b0, c0, d0

        # Vòng lặp chính của thuật toán MD5
        for j in range(64):
            if 0 <= j <= 15:
                f = (b & c) | ((~b) & d)
                g = j
            elif 16 <= j <= 31:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif 32 <= j <= 47:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else: # 48 <= j <= 63
                f = c ^ (b | (~d))
                g = (7 * j) % 16
            
            f = (f + a + k[j] + words[g]) & 0xFFFFFFFF
            a = d
            d = c
            c = b
            b = (b + left_rotate(f, s[j])) & 0xFFFFFFFF

        # Cộng dồn kết quả vào các biến ban đầu
        a0 = (a0 + a) & 0xFFFFFFFF
        b0 = (b0 + b) & 0xFFFFFFFF
        c0 = (c0 + c) & 0xFFFFFFFF
        d0 = (d0 + d) & 0xFFFFFFFF

    # Kết hợp các giá trị cuối cùng để tạo ra mã hash
    final_hash = [a0, b0, c0, d0]
    return b''.join(val.to_bytes(4, 'little') for val in final_hash)

if __name__ == "__main__":
    input_string = input("Nhập chuỗi cần băm: ")
    md5_hash_bytes = md5(input_string.encode('utf-8'))
    md5_hash = md5_hash_bytes.hex()
    
    print(f"Mã băm MD5 của chuỗi '{input_string}' là: {md5_hash}")