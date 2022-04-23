import socket

# sock = socket.socket()
#
# #서버로 연결 요청
# sock.connect(
#     ('127.0.0.1', 3000)
# )
#
# while True:
#     msg = input('message:')
#     sock.send(bytes(msg, encoding='utf8'))
#
#     data = sock.recv(255)
#     msg = data.decode(encoding='utf8')
#     print("server:", msg)
import threading, time
class SocketClient:
    def __init__(self, address: str, port: int):
        self.addr = address
        self.port = port
        self.sock = socket.socket()

    def send(self):
        while True:
            msg = input()
            self.sock.send(bytes(msg, encoding='utf8'))

    def recv(self):
        while True:
            data = self.sock.recv(225)
            msg = data.decode(encoding='utf8')
            print(msg)
    def communicate(self):
        self.sock.connect(
            (self.addr, self.port)
        )

        t_send = threading.Thread(target=self.send, daemon=True)
        t_recv = threading.Thread(target=self.recv, daemon=True)
        t_send.start()
        t_recv.start()
        while True:
            time.sleep(1000)

client = SocketClient('127.0.0.1', 3000)
client.communicate()
