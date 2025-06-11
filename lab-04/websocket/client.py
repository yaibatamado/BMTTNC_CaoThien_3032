import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None
        self.io_loop = io_loop

    def start(self):
        """Bắt đầu quá trình kết nối."""
        self.connect_and_read()

    def stop(self):
        self.io_loop.stop()

    def connect_and_read(self):
        """Kết nối tới server và bắt đầu đọc tin nhắn."""
        print("Connecting...")
        tornado.websocket.websocket_connect(
            url=f"ws://localhost:8888/websocket",
            callback=self.maybe_retry_connection, # Callback khi kết nối xong
            on_message_callback=self.on_message, # Callback khi có tin nhắn
            ping_interval=10,
            ping_timeout=30,
        )

    def maybe_retry_connection(self, future):
        """Xử lý kết quả kết nối, thử lại nếu thất bại."""
        try:
            self.connection = future.result()
            print("Connected successfully!")
        except:
            print("Could not connect, retrying in 3 seconds...")
            self.io_loop.call_later(3, self.connect_and_read)

    def on_message(self, message):
        """Xử lý khi nhận được tin nhắn từ server."""
        if message is None:
            print("Disconnected, reconnecting...")
            self.connect_and_read()
            return

        print(f"Received word from server: {message}")
        # Tiếp tục lắng nghe tin nhắn tiếp theo
        # self.connection.read_message(callback=self.on_message) # Dòng này không cần thiết vì on_message_callback đã xử lý

def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)

    # Thêm callback để chạy client.start() khi IOLoop bắt đầu
    io_loop.add_callback(client.start)
    io_loop.start()

if __name__ == "__main__":
    main()