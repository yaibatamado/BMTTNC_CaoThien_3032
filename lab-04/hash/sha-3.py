from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hashed_text = sha3(text)
    print(f"Chuỗi văn bản đã nhập: {text.decode('utf-8')}")
    print(f"SHA-3 Hash: {hashed_text.hexdigest()}")

if __name__ == "__main__":
    main()