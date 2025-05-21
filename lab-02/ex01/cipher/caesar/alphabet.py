# cipher/caesar/alphabet.py

# Bảng chữ cái tiếng Anh viết thường
LOWERCASE_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# Bảng chữ cái tiếng Anh viết hoa
UPPERCASE_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Các chữ số
DIGITS = '0123456789'

# Các ký tự đặc biệt thường dùng (có thể mở rộng nếu cần)
# Lưu ý: Việc mã hóa ký tự đặc biệt có thể phức tạp hơn và
# không phải lúc nào cũng tuân theo quy tắc dịch chuyển đơn giản.
# Trong bài này, chúng ta có thể chọn bỏ qua chúng hoặc xử lý theo cách riêng.
# Hiện tại, chúng ta sẽ tập trung vào chữ cái và chữ số.
# SPECIAL_CHARACTERS = ' .,!?'

# Tổng số ký tự trong bảng chữ cái (chỉ tính chữ thường)
ALPHABET_SIZE = len(LOWERCASE_ALPHABET)

if __name__ == '__main__':
    print(f"Lowercase Alphabet: {LOWERCASE_ALPHABET}")
    print(f"Uppercase Alphabet: {UPPERCASE_ALPHABET}")
    print(f"Digits: {DIGITS}")
    print(f"Alphabet Size (lowercase): {ALPHABET_SIZE}")
