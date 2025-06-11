from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def generate_dh_parameters():
    # Tạo các tham số chung cho việc trao đổi khóa
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    return parameters

def generate_server_key_pair(parameters):
    # Server tạo khóa riêng và khóa công khai từ các tham số chung
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def main():
    # 1. Tạo tham số DH
    parameters = generate_dh_parameters()

    # 2. Tạo cặp khóa cho server
    private_key, public_key = generate_server_key_pair(parameters)

    # 3. Lưu khóa công khai của server vào file 'server_public_key.pem'
    # Client sẽ đọc file này để thực hiện việc trao đổi khóa
    with open("server_public_key.pem", "wb") as f:
        f.write(public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    print("Server public key has been generated and saved to server_public_key.pem")

if __name__ == "__main__":
    main()