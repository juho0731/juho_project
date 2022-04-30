import socket

# sock = socket.socket()
#
# #클라이언트가 연결한 주소 바인딩
# #port: 종당간 통신의 출입구
# sock.bind(
#     ('127.0.0.1', 3000)
# )
#
# # 클라이언트 연결 대기 모드
# #파라미터 값은 연결 큐의 최대 크기를 의미
# sock.listen(5)
#
# # 이 라인에서 대기하면서 클라이언트 측의 연결 요청을 기다림
# # 연결이 되면 클라이언트 소켓과 주고를 반함
# client_sock, address = sock.accept()
#
# print(address, '에서 연결 요청')
#
# while True:
#     # 최대 255개의 길이의 데이터를 수신
#     data = client_sock.recv(255)
#     msg = data.decode(encoding='utf8')
#     print("message:", msg)
#
#     msg = input('server')
#     client_sock.send(bytes(msg, encoding='utf8'))
import socket
# 스레드를 사용하기 위한 모듈
import threading
import time

class SocketServer:
    def __init__(self, address, port):
        #바인딩할 주소와 포트번호
        self.addr = address
        self.port = port

        #소켓 생성
        self.sock = socket.socket()

        #클라이언트 소켓 리스트
        self.clients = []

    def accept(self):
        self.sock.bind(
            (self.addr, self.port)
        )
        self.sock.listen(5)
        while True:
            client_sock, address = self.sock.accept()
            client_sock.settimeout(0.01)
            self.clients.append(client_sock)
            print(address, '에서 연결')

    # 클라이언트 소켓에 데이터 전송
    def send(self, msg):

        for c in self.clients:
            try:
                c.send(bytes(msg, encoding='utf8'))
            except TimeoutError:
                continue
            except ConnectionResetError:
                continue
            except ConnectionAbortedError:
                continue

    # 클라이언트 소켓으로 부터 데이터 수신
    def recv(self):
        while True:
            for c in self.clients:
                try:
                    data = c.recv(255)
                    msg = data.decode(encoding='utf8')
                    print(msg)
                    self.send(msg)
                except socket.timeout:
                    continue
                except ConnectionResetError:
                    del c
                except ConnectionAbortedError:
                    del c
    #통신 시작 함수
    def communicate(self):
        #각자의 스레드 생성
        t_accept = threading.Thread(target=self.accept, daemon=True)
        t_recv = threading.Thread(target=self.recv, daemon=True)

        # 스레드 시작
        t_accept.start()
        t_recv.start()

        # 프로그램 종료 방지
        while True:
            time.sleep(1000)


server = SocketServer('127.0.0.1', 3000)
server.communicate()