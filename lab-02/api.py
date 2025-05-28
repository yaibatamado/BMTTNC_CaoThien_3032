from cipher.transposition import TranspositionCipher
from cipher.playfair import PlayFairCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# Khởi tạo các đối tượng cipher
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
playfair_cipher = PlayFairCipher()
railfence_cipher = RailFenceCipher()
transposition_cipher = TranspositionCipher()

# --- Caesar Cipher API Endpoints ---
@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    try:
        key = int(data.get('key'))
    except (ValueError, TypeError):
        return jsonify({'error': 'Key must be an integer.'}), 400
    if plain_text is None:
        return jsonify({'error': 'Missing plain_text.'}), 400
        
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    try:
        key = int(data.get('key'))
    except (ValueError, TypeError):
        return jsonify({'error': 'Key must be an integer.'}), 400
    if cipher_text is None:
        return jsonify({'error': 'Missing cipher_text.'}), 400

    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# --- Vigenere Cipher API Endpoints ---
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = data.get('key')
    if plain_text is None or key is None:
        return jsonify({'error': 'Missing plain_text or key.'}), 400
    if not isinstance(key, str) or not key.isalpha():
        return jsonify({'error': 'Key must be a string containing only alphabetic characters.'}), 400

    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    if cipher_text is None or key is None:
        return jsonify({'error': 'Missing cipher_text or key.'}), 400
    if not isinstance(key, str) or not key.isalpha():
        return jsonify({'error': 'Key must be a string containing only alphabetic characters.'}), 400

    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# --- Playfair Cipher API Endpoints ---
@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = data.get('key')
    if plain_text is None or key is None:
        return jsonify({'error': 'Missing plain_text or key.'}), 400
    if not isinstance(key, str) or not key.isalpha(): # Đơn giản hóa kiểm tra khóa cho API
        return jsonify({'error': 'Key must be a string containing only alphabetic characters for matrix generation.'}), 400

    try:
        matrix = playfair_cipher.create_playfair_matrix(key)
        encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)
        return jsonify({'encrypted_text': encrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = data.get('key')
    if cipher_text is None or key is None:
        return jsonify({'error': 'Missing cipher_text or key.'}), 400
    if not isinstance(key, str) or not key.isalpha():
        return jsonify({'error': 'Key must be a string containing only alphabetic characters for matrix generation.'}), 400

    try:
        matrix = playfair_cipher.create_playfair_matrix(key)
        decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)
        return jsonify({'decrypted_text': decrypted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# --- Rail Fence Cipher API Endpoints ---
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    try:
        key = int(data.get('key')) # Số hàng (rails)
    except (ValueError, TypeError):
        return jsonify({'error': 'Key (number of rails) must be an integer.'}), 400
    if plain_text is None:
        return jsonify({'error': 'Missing plain_text.'}), 400
    if key <= 1:
        return jsonify({'error': 'Key (number of rails) must be greater than 1.'}), 400
        
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    try:
        key = int(data.get('key')) # Số hàng (rails)
    except (ValueError, TypeError):
        return jsonify({'error': 'Key (number of rails) must be an integer.'}), 400
    if cipher_text is None:
        return jsonify({'error': 'Missing cipher_text.'}), 400
    if key <= 1:
        return jsonify({'error': 'Key (number of rails) must be greater than 1.'}), 400

    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# --- Transposition Cipher API Endpoints (đã có từ trước) ---
@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key_str = data.get('key')
    if plain_text is None or key_str is None:
        return jsonify({'error': 'Missing plain_text or key.'}), 400
    try:
        key = int(key_str)
    except ValueError:
        return jsonify({'error': 'Key must be an integer.'}), 400
    if key <= 0:
         return jsonify({'error': 'Key must be a positive integer.'}), 400

    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key_str = data.get('key')
    if cipher_text is None or key_str is None:
        return jsonify({'error': 'Missing cipher_text or key.'}), 400
    try:
        key = int(key_str)
    except ValueError:
        return jsonify({'error': 'Key must be an integer.'}), 400
    if key <= 0:
         return jsonify({'error': 'Key must be a positive integer.'}), 400

    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
