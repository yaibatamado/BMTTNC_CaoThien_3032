import sys
from PIL import Image

def encode_image(image_path, message):
    """Giấu một thông điệp vào trong ảnh sử dụng kỹ thuật LSB."""
    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file ảnh tại '{image_path}'")
        return

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110' 

    if len(binary_message) > img.size[0] * img.size[1] * 3:
        print("Lỗi: Thông điệp quá dài để giấu trong ảnh này.")
        return

    data_index = 0
    for row in range(img.height):
        for col in range(img.width):
            pixel = list(img.getpixel((col, row)))

            for color_channel in range(3):
                if data_index < len(binary_message):
                    pixel[color_channel] = int(format(pixel[color_channel], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
            
            img.putpixel((col, row), tuple(pixel))
            
            if data_index >= len(binary_message):
                break
        if data_index >= len(binary_message):
            break

    encoded_image_path = 'encoded_image.png'
    img.save(encoded_image_path)
    print(f"Steganography complete. Encoded image saved as '{encoded_image_path}'")

def main():
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <image_path> \"<message>\"")
        print("Lưu ý: Đặt thông điệp trong dấu ngoặc kép nếu có khoảng trắng.")
        return

    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == "__main__":
    main()