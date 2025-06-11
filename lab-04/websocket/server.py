import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketServer(tornado.websocket.WebSocketHandler):
    # Một tập hợp (set) để lưu trữ tất cả các client đang kết nối
    clients = set()

    def open(self):
        """Được gọi khi một client mới kết nối."""
        WebSocketServer.clients.add(self)
        print(f"New client connected. Total clients: {len(WebSocketServer.clients)}")

    def on_close(self):
        """Được gọi khi một client ngắt kết nối."""
        WebSocketServer.clients.remove(self)
        print(f"Client disconnected. Total clients: {len(WebSocketServer.clients)}")

    @classmethod
    def send_message(cls, message: str):
        """Gửi tin nhắn tới tất cả các client đang kết nối."""
        print(f"Sending message '{message}' to {len(cls.clients)} client(s).")
        for client in cls.clients:
            client.write_message(message)

class RandomWordSelector:
    """Lớp trợ giúp để chọn một từ ngẫu nhiên từ danh sách."""
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(self):
        return random.choice(self.word_list)

def main():
    # Tạo ứng dụng Tornado và định tuyến
    app = tornado.web.Application([
        (r"/websocket", WebSocketServer),
    ],
        # Ping để giữ kết nối không bị đóng do timeout
        websocket_ping_interval=10,
        websocket_ping_timeout=30,
    )
    app.listen(8888)
    print("Server is listening on port 8888...")

    io_loop = tornado.ioloop.IOLoop.current()

    # Danh sách các loại trái cây
    word_selector = RandomWordSelector(['apple', 'banana', 'orange', 'grape', 'melon'])

    # Tạo một callback định kỳ để gửi tin nhắn mỗi 3000ms (3 giây)
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()), 3000
    )

    periodic_callback.start()
    io_loop.start()

if __name__ == "__main__":
    main()