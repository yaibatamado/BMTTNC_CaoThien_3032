# api.py
import os
from flask import Flask, request, jsonify
# from dotenv import load_dotenv # Đã xóa dòng này
from cipher.caesar import caesar_encrypt, caesar_decrypt # Import từ package đã tạo

# Tải các biến môi trường từ tệp .env (nếu có)
# load_dotenv() # Đã xóa dòng này

app = Flask(__name__)

# Cấu hình (có thể đặt trong .env)
# Ví dụ: app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/')
def home():
    return "Caesar Cipher API is running!"

@app.route('/api/caesar/encrypt', methods=['POST'])
def encrypt_route():
    """
    Endpoint API để mã hóa văn bản.
    Nhận JSON payload: {"plain_text": "some text", "key": 3}
    Trả về JSON: {"cipher_text": "encrypted text"}
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        plain_text = data.get('plain_text')
        key_str = data.get('key')

        if plain_text is None or key_str is None:
            return jsonify({"error": "Missing 'plain_text' or 'key' in request"}), 400
        
        if not isinstance(plain_text, str):
            return jsonify({"error": "'plain_text' must be a string"}), 400

        try:
            key = int(key_str)
        except ValueError:
            return jsonify({"error": "'key' must be an integer"}), 400

        cipher_text = caesar_encrypt(plain_text, key)
        return jsonify({"cipher_text": cipher_text}), 200

    except Exception as e:
        # Ghi log lỗi ở đây nếu cần thiết
        # import logging
        # logging.error(f"Error in /encrypt: {e}")
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/api/caesar/decrypt', methods=['POST'])
def decrypt_route():
    """
    Endpoint API để giải mã văn bản.
    Nhận JSON payload: {"cipher_text": "encrypted text", "key": 3}
    Trả về JSON: {"plain_text": "decrypted text"}
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400

        cipher_text = data.get('cipher_text')
        key_str = data.get('key')

        if cipher_text is None or key_str is None:
            return jsonify({"error": "Missing 'cipher_text' or 'key' in request"}), 400

        if not isinstance(cipher_text, str):
            return jsonify({"error": "'cipher_text' must be a string"}), 400
            
        try:
            key = int(key_str)
        except ValueError:
            return jsonify({"error": "'key' must be an integer"}), 400

        plain_text = caesar_decrypt(cipher_text, key)
        return jsonify({"plain_text": plain_text}), 200
        
    except Exception as e:
        # logging.error(f"Error in /decrypt: {e}")
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    # Chạy Flask development server
    # debug=True sẽ tự động reload server khi có thay đổi code
    # host='0.0.0.0' cho phép truy cập từ các máy khác trong cùng mạng
    # Bây giờ, nếu biến môi trường PORT không được đặt, nó sẽ mặc định là 5000.
    # Bạn có thể đặt biến môi trường PORT trước khi chạy nếu muốn dùng port khác.
    # Ví dụ: PORT=8080 python api.py
    port = int(os.environ.get("PORT", 5000)) 
    app.run(debug=True, host='0.0.0.0', port=port)
