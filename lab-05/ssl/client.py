import socket
import ssl
import threading

server_address = ('localhost', 12345)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print(f"\nNhận: {data.decode('utf-8')}\nNhập tin nhắn: ", end="")
    except:
        pass
    finally:
        ssl_socket.close()
        print("Kết nối đã đóng.")

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
ssl_socket.connect(server_address)
print("Đã kết nối SSL tới server.")

receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
receive_thread.start()

try:
    while True:
        message = input("Nhập tin nhắn: ")
        if message.lower() == 'exit':
            break
        ssl_socket.send(message.encode('utf-8'))
except KeyboardInterrupt:
    print("\nĐang đóng client...")
finally:
    ssl_socket.close()