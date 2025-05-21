# cipher/caesar/caesar_cipher.py

from .alphabet import LOWERCASE_ALPHABET, UPPERCASE_ALPHABET, DIGITS, ALPHABET_SIZE

def caesar_encrypt(plain_text: str, key: int) -> str:
    """
    Mã hóa văn bản bằng thuật toán Caesar.

    Args:
        plain_text (str): Văn bản gốc cần mã hóa.
        key (int): Khóa dịch chuyển (số ký tự sẽ dịch chuyển).

    Returns:
        str: Văn bản đã được mã hóa.
    """
    cipher_text = []
    for char in plain_text:
        if char in LOWERCASE_ALPHABET:
            # Xử lý chữ thường
            start_index = LOWERCASE_ALPHABET.find(char)
            new_index = (start_index + key) % ALPHABET_SIZE
            cipher_text.append(LOWERCASE_ALPHABET[new_index])
        elif char in UPPERCASE_ALPHABET:
            # Xử lý chữ hoa
            start_index = UPPERCASE_ALPHABET.find(char)
            new_index = (start_index + key) % ALPHABET_SIZE
            cipher_text.append(UPPERCASE_ALPHABET[new_index])
        elif char in DIGITS:
            # Xử lý chữ số (dịch chuyển trong phạm vi 0-9)
            # Lưu ý: Kích thước bảng chữ số là 10
            digit_alphabet_size = len(DIGITS)
            start_index = DIGITS.find(char)
            new_index = (start_index + key) % digit_alphabet_size
            cipher_text.append(DIGITS[new_index])
        else:
            # Giữ nguyên các ký tự không thuộc bảng chữ cái (ví dụ: dấu cách, ký tự đặc biệt)
            cipher_text.append(char)
    return "".join(cipher_text)

def caesar_decrypt(cipher_text: str, key: int) -> str:
    """
    Giải mã văn bản đã được mã hóa bằng thuật toán Caesar.

    Args:
        cipher_text (str): Văn bản đã mã hóa.
        key (int): Khóa dịch chuyển (phải giống với khóa đã dùng để mã hóa).

    Returns:
        str: Văn bản gốc đã được giải mã.
    """
    # Giải mã thực chất là mã hóa với khóa âm (hoặc khóa = ALPHABET_SIZE - key)
    # Tuy nhiên, để đơn giản và rõ ràng, chúng ta sẽ dịch chuyển ngược lại.
    plain_text = []
    for char in cipher_text:
        if char in LOWERCASE_ALPHABET:
            start_index = LOWERCASE_ALPHABET.find(char)
            new_index = (start_index - key) % ALPHABET_SIZE
            plain_text.append(LOWERCASE_ALPHABET[new_index])
        elif char in UPPERCASE_ALPHABET:
            start_index = UPPERCASE_ALPHABET.find(char)
            new_index = (start_index - key) % ALPHABET_SIZE
            plain_text.append(UPPERCASE_ALPHABET[new_index])
        elif char in DIGITS:
            digit_alphabet_size = len(DIGITS)
            start_index = DIGITS.find(char)
            new_index = (start_index - key) % digit_alphabet_size
            plain_text.append(DIGITS[new_index])
        else:
            plain_text.append(char)
    return "".join(plain_text)

if __name__ == '__main__':
    # Ví dụ kiểm tra
    text1 = "Hello World 123!"
    key1 = 3
    encrypted_text1 = caesar_encrypt(text1, key1)
    decrypted_text1 = caesar_decrypt(encrypted_text1, key1)

    print(f"Original:    '{text1}'")
    print(f"Key:         {key1}")
    print(f"Encrypted:   '{encrypted_text1}'") # Dự kiến: 'Khoor Zruog 456!'
    print(f"Decrypted:   '{decrypted_text1}'") # Dự kiến: 'Hello World 123!'
    print("-" * 20)

    text2 = "PYTHON"
    key2 = 5
    encrypted_text2 = caesar_encrypt(text2, key2)
    decrypted_text2 = caesar_decrypt(encrypted_text2, key2)

    print(f"Original:    '{text2}'")
    print(f"Key:         {key2}")
    print(f"Encrypted:   '{encrypted_text2}'") # Dự kiến: 'UDYMTS'
    print(f"Decrypted:   '{decrypted_text2}'") # Dự kiến: 'PYTHON'
    print("-" * 20)

    text3 = "Caesar Cipher Test 007"
    key3 = 7
    encrypted_text3 = caesar_encrypt(text3, key3)
    decrypted_text3 = caesar_decrypt(encrypted_text3, key3)
    print(f"Original:    '{text3}'")
    print(f"Key:         {key3}")
    print(f"Encrypted:   '{encrypted_text3}'")
    print(f"Decrypted:   '{decrypted_text3}'")

