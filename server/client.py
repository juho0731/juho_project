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

    def send(self, msg):
        self.sock.send(bytes(msg, encoding='utf8'))

    def recv(self, callback):
        while True:
            data = self.sock.recv(225)
            msg = data.decode(encoding='utf8')
            #메시지 수신후 콜백함수로 전달
            callback(msg)

    def connect(self):
        self.sock.connect(
            (self.addr, self.port)
        )

