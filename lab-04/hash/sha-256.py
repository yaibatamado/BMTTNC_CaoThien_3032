import hashlib

def calculate_sha256_hash(data):
    sha256_hash = hashlib.sha256()
    # Chuyển đổi dữ liệu thành bytes và cập nhật vào đối tượng hash
    sha256_hash.update(data.encode('utf-8')) 
    # Trả về biểu diễn hex của chuỗi hash
    return sha256_hash.hexdigest()

data_to_hash = input("Nhập dữ liệu để hash bằng SHA-256: ")
hash_value = calculate_sha256_hash(data_to_hash)
print(f"Giá trị hash SHA-256: {hash_value}")