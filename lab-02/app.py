from flask import Flask, render_template, request, flash

# Import các lớp cipher từ thư mục cipher của bạn
from cipher.caesar import CaesarCipher #
from cipher.vigenere import VigenereCipher #
from cipher.playfair import PlayFairCipher #
from cipher.railfence import RailFenceCipher #
from cipher.transposition import TranspositionCipher #

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # Cần thiết cho flash messages

# Khởi tạo các đối tượng cipher
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
playfair_cipher = PlayFairCipher()
railfence_cipher = RailFenceCipher()
transposition_cipher = TranspositionCipher()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar', methods=['GET', 'POST'])
def caesar():
    if request.method == 'POST':
        text = request.form['text']
        try:
            key = int(request.form['key'])
        except ValueError:
            flash('Khóa phải là một số nguyên!', 'error')
            return render_template('caesar.html', current_text=text, key='')
        
        action = request.form['action']
        result = ''

        if not text:
            flash('Văn bản không được để trống!', 'error')
        elif action == 'encrypt':
            result = caesar_cipher.encrypt_text(text, key) #
            flash(f'Văn bản đã mã hóa: {result}', 'success')
        elif action == 'decrypt':
            result = caesar_cipher.decrypt_text(text, key) #
            flash(f'Văn bản đã giải mã: {result}', 'success')
        return render_template('caesar.html', current_text=text, key=key, result=result)
    return render_template('caesar.html')

@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere():
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        action = request.form['action']
        result = ''

        if not text:
            flash('Văn bản không được để trống!', 'error')
        elif not key or not key.isalpha():
            flash('Khóa không được để trống và chỉ chứa các chữ cái!', 'error')
        elif action == 'encrypt':
            result = vigenere_cipher.vigenere_encrypt(text, key) #
            flash(f'Văn bản đã mã hóa: {result}', 'success')
        elif action == 'decrypt':
            result = vigenere_cipher.vigenere_decrypt(text, key) #
            flash(f'Văn bản đã giải mã: {result}', 'success')
        return render_template('vigenere.html', current_text=text, key=key, result=result)
    return render_template('vigenere.html')

@app.route('/playfair', methods=['GET', 'POST'])
def playfair():
    if request.method == 'POST':
        text = request.form['text']
        key = request.form['key']
        action = request.form['action']
        result = ''

        if not text:
            flash('Văn bản không được để trống!', 'error')
        elif not key or not key.isalpha():
            flash('Khóa không được để trống và chỉ chứa các chữ cái!', 'error')
        else:
            try:
                matrix = playfair_cipher.create_playfair_matrix(key) #
                if action == 'encrypt':
                    result = playfair_cipher.playfair_encrypt(text, matrix) #
                    flash(f'Văn bản đã mã hóa: {result}', 'success')
                elif action == 'decrypt':
                    result = playfair_cipher.playfair_decrypt(text, matrix) #
                    flash(f'Văn bản đã giải mã: {result}', 'success')
            except Exception as e:
                flash(f'Đã xảy ra lỗi: {e}', 'error')
        return render_template('playfair.html', current_text=text, key=key, result=result)
    return render_template('playfair.html')

@app.route('/railfence', methods=['GET', 'POST'])
def railfence():
    if request.method == 'POST':
        text = request.form['text']
        try:
            key = int(request.form['key']) # Số lượng "rails"
        except ValueError:
            flash('Khóa (số hàng) phải là một số nguyên!', 'error')
            return render_template('railfence.html', current_text=text, key='')

        action = request.form['action']
        result = ''

        if not text:
            flash('Văn bản không được để trống!', 'error')
        elif key <= 1:
            flash('Khóa (số hàng) phải lớn hơn 1!', 'error')
        elif action == 'encrypt':
            result = railfence_cipher.rail_fence_encrypt(text, key) #
            flash(f'Văn bản đã mã hóa: {result}', 'success')
        elif action == 'decrypt':
            result = railfence_cipher.rail_fence_decrypt(text, key) #
            flash(f'Văn bản đã giải mã: {result}', 'success')
        return render_template('railfence.html', current_text=text, key=key, result=result)
    return render_template('railfence.html')

@app.route('/transposition', methods=['GET', 'POST'])
def transposition():
    if request.method == 'POST':
        text = request.form['text']
        try:
            key = int(request.form['key'])
        except ValueError:
            flash('Khóa phải là một số nguyên!', 'error')
            return render_template('transposition.html', current_text=text, key='')
        
        action = request.form['action']
        result = ''

        if not text:
            flash('Văn bản không được để trống!', 'error')
        elif key <= 0 : # Hoặc một ràng buộc hợp lý khác cho khóa transposition
             flash('Khóa phải là số dương!', 'error')
        elif action == 'encrypt':
            result = transposition_cipher.encrypt(text, key) #
            flash(f'Văn bản đã mã hóa: {result}', 'success')
        elif action == 'decrypt':
            result = transposition_cipher.decrypt(text, key) #
            flash(f'Văn bản đã giải mã: {result}', 'success')
        return render_template('transposition.html', current_text=text, key=key, result=result)
    return render_template('transposition.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)