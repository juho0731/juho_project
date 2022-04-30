from tkinter import *
from tkinter.ttk import *

import client
from client import *
import threading

class Chat:
    def __init__(self):
        # 클라이언트 소켓 생성
        self.client = SocketClient('127.0.0.1', 3000)
        #receive 스레드
        self.t_recv = None

        # UI 생성
        #윈도우 생성
        self.root = Tk()
        self.root.title("채팅 클라이언트")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        # 주소 입력란 생성
        # 1.UI 배치를 위한 프레임 생성
        self.frame1 = Frame(self.root)
        self.frame1.pack(side="top", padx=5, pady=5, fill="x")
        # 2. 서버 주소 입력창 생성
        self.address_box = Entry(self.frame1)
        self.address_box.pack(side="left", padx=5, expand=True, fill="both")

        self.connect_btn = Button(self.frame1, text="연결")
        self.connect_btn.pack(side="right", padx=5, fill="both")

        # 채팅 입력창 생성
        # 1. UI 배치를 위한 프레임 생성
        self.frame2 = Frame(self.root)
        self.frame2.pack(side="top", padx=5, pady=5, expand=True, fill="both")

        self.scroll = Scrollbar(self.frame2)
        self.scroll.pack(side="right", fill="y")

        self.chat_box = Listbox(self.frame2, yscrollcommand=self.scroll.set)
        self.chat_box.pack(side="left", expand=True, fill="both")
        self.scroll.configure(command=self.chat_box.yview)

        self.frame3 = Frame(self.root)
        self.frame3.pack(side="bottom", padx=5, pady=5, fill="x")
        # 2. 이름 입력창 생성
        self.name_box = Entry(self.frame3, state="disabled", width=10)
        self.name_box.pack(side="left", fill="both")
        # 3.내용 입력창 새성
        self.input_box = Entry(self.frame3, state=DISABLED)
        self.input_box.pack(side="left", expand=True, fill="both", padx=5)
        # 4.전송 버트 생성
        self.send_btn = Button(self.frame3, text="전송", state=DISABLED)
        self.send_btn.pack(side="right", fill="both")
        # UI 생성 끝

        self.connect_btn.configure(command=self.cmd_connect)
        self.send_btn.configure(command=self.cmd_send)
        self.input_box.bind("<Return>", lambda x: self.cmd_send())

        self.root.mainloop()

    def callback_recv(self, msg):
        if type(msg) == str:
            scrollPos = self.chat_box.yview()[1]
            #메세지를 리스트에 추가
            self.chat_box.insert(END, msg)
            if scrollPos == 1.0:
                self.chat_box.yview_moveto(1.0)

    def cmd_connect(self):
        try:
            #입력된 주소를 가져옴
            addr_str = self.address_box.get()
            #ip 주소와 port를 따로 분리시킴
            ip, port = addr_str.split(":")
            #SockClient의 연결정보 수정
            self.client.addr = ip
            self.client.port = int(port)
            #연결 시작
            self.client.connect()
            self.t_recv = threading.Thread(target=self.client.recv, args=(self.callback_recv,))
            self.t_recv.start()
        except Exception:
            #연결이 실패하면 그냥 무시
            pass
        else:
            self.address_box.configure(state="disabled")
            self.connect_btn.configure(state="disabled")
            self.name_box.configure(state="enabled")
            self.input_box.configure(state="enabled")
            self.send_btn.configure(state="enabled")

    # 전송 커맨드 (서버로 메시지 전송, 전송 버튼에 할당할 것)
    def cmd_send(self):
        try:
            # 이름과 메세지를 입력창으로 부터 읽는다.
            name = self.name_box.get()
            msg = self.input_box.get()
            if len(name) == 0:
                name = ("익명")
            if len(msg) == 0:
                return
            #입력된 이름과 내용으로 메세지 전송
            self.client.send(name + ":" + msg)
        except Exception:
            pass
        else:
            self.input_box.delete(0, END)



Chat()
