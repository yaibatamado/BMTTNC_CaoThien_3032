import hashlib

def blake2(message):
    # digest_size=64 là mặc định cho blake2b
    blake2_hash = hashlib.blake2b(digest_size=64) 
    blake2_hash.update(message)
    return blake2_hash

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hashed_text = blake2(text)
    print(f"Chuỗi văn bản đã nhập: {text.decode('utf-8')}")
    print(f"BLAKE2 Hash: {hashed_text.hexdigest()}")

if __name__ == "__main__":
    main()