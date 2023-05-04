import tkinter as tk
from tkinter.font import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
def evaluate(cal):
    cal = cal.split("x")
    if not cal[0]:
        cal[0] = 1
    elif cal[0] == '-':
        cal[0] = -1
    if not cal[1]:
        cal[1] = 0
    a, b = map(int, cal)
    return a, b

def draw_graph():
    # 입력된 함수식을 가져와 계산하기
    func = func_entry.get()
    a, b = evaluate(func)
    x = np.array(range(-20, 21))
    y = a*x+b
    # 그래프 그리기
    ax.plot(x, y, "-o")
    # 그래프 출력하기
    canvas.draw()
    arr_btn1 = [Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9]
    x_range = list(range(-20, 21, 5))
    for i in range(len(arr_btn1)):
        arr_btn1[i].config(text=a*x_range[i]+b)

def compare_graph():
    # 입력된 함수식을 가져와 계산하기
    a, b = evaluate(func_entry.get())
    a2 = int(entA2.get())
    b2 = int(entB2.get())
    x = np.array(range(-20, 21))
    y = (a+a2)*x + (b+b2)
    # 그래프 그리기
    ax.plot(x, y, marker="o")
    # 그래프 출력하기
    canvas.draw()
    arr_btn2 = [Y12, Y22, Y32, Y42, Y52,Y62, Y72, Y82, Y92]
    x_range = list(range(-20, 21, 5))
    for i in range(len(arr_btn2)):
        arr_btn2[i].config(text=a * x_range[i] + b)
def graph_init():
    ax.set_xlim([-20, 20])
    ax.set_ylim([-20, 20])
    ax.spines["bottom"].set_position(('data', 0))
    ax.spines['left'].set_position(("data", 0))
    ax.grid(color='0.8')

window = tk.Tk()
window.title("1차함수 그래프")
window.geometry('600x750')
font = Font(family="맑은 고딕", size=15)
#  프레임
frame = tk.Frame(window)
frame.grid(row = 0, column=0, columnspan=3)

# 그래프 기본창
fig = Figure(figsize=(6, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=frame)
graph_init()
canvas.draw()
canvas.get_tk_widget().grid(row=2, column=0, columnspan=3)

# 함수 입력창 생성
func_label = tk.Label(text="1차함수 입력: ", font = font)
func_label.grid(row=1, column=0)
func_entry = tk.Entry(window, font=Font(family="맑은고딕", size=20), width=15)
func_entry.grid(row=1, column=1)
func_entry.insert(0, "ax+b")

LabelX2 = tk.Label(window, text= "x계수 변화량", font=font)
LabelX2.grid(row=2, column=0, padx=20)
entA2 = tk.Entry(window, font = font, width=10)
entA2.grid(row=2, column=1, padx=20)
entA2.insert(0, '0')

LabelY2 = tk.Label(window, text= "Y절편 변화량", font=font)
LabelY2.grid(row=3, column=0, padx=20)
entB2 = tk.Entry(window, font = font, width=10)
entB2.grid(row=3, column=1, padx=20)
entB2.insert(0, '0')

# 그래프 그리기 버튼 생성
draw_button = tk.Button(window, text='그래프 그리기', font=font, command=draw_graph)
draw_button.grid(row=1, column=2, padx=20)
compare_button = tk.Button(window, text='비교하기', font=font, command=compare_graph)
compare_button.grid(row=2, column=2, rowspan=2, padx=2)

# 그래프 비교표
frame2 = tk.Frame(window)
frame2.grid(row=4, column=0, columnspan=4)

#비교 전
nothing = tk.Label(frame2, text='', width=4, relief="solid", font= font)
nothing.grid(row=0, column=0, sticky='wens')
before = tk.Label(frame2, text= "변경전 ", relief="solid", font = font)
before.grid(row=0, column=1, columnspan=9, sticky='wens')
strX = tk.Label(frame2, text= "X값 ", width=4, relief="solid", font = font)
strX.grid(row=1, column=0, sticky='wens')

X1 = tk.Label(frame2, text='-20', width=4, relief='solid', font=font)
X2 =tk.Label(frame2, text='-15', width=4, relief='solid', font=font)
X3 =tk.Label(frame2, text='-10', width=4, relief='solid', font=font)
X4 = tk.Label(frame2, text='-5', width=4, relief='solid', font=font)
X5 =tk.Label(frame2, text='0', width=4, relief='solid', font=font)
X6 = tk.Label(frame2, text='5', width=4, relief='solid', font=font)
X7 = tk.Label(frame2, text='10', width=4, relief='solid', font=font)
X8 = tk.Label(frame2, text='15', width=4, relief='solid', font=font)
X9 =tk.Label(frame2, text='20', width=4, relief='solid', font=font)

X1.grid(row=1, column=1, sticky='wens')
X2.grid(row=1, column=2, sticky='wens')
X3.grid(row=1, column=3, sticky='wens')
X4.grid(row=1, column=4, sticky='wens')
X5.grid(row=1, column=5, sticky='wens')
X6.grid(row=1, column=6, sticky='wens')
X7.grid(row=1, column=7, sticky='wens')
X8.grid(row=1, column=8, sticky='wens')
X9.grid(row=1, column=9, sticky='wens')

strY =tk.Label(frame2, text = 'Y값', width=4, relief="solid", font= font)
Y1 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y2 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y3 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y4 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y5 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y6 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y7 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y8 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y9 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)

strY.grid(row=2, column=0, sticky='wens')
Y1.grid(row=2, column=1, sticky='wens')
Y2.grid(row=2, column=2, sticky='wens')
Y3.grid(row=2, column=3, sticky='wens')
Y4.grid(row=2, column=4, sticky='wens')
Y5.grid(row=2, column=5, sticky='wens')
Y6.grid(row=2, column=6, sticky='wens')
Y7.grid(row=2, column=7, sticky='wens')
Y8.grid(row=2, column=8, sticky='wens')
Y9.grid(row=2, column=9, sticky='wens')

# 비교 후

nothing2 = tk.Label(frame2, text='', width=4, relief="solid", font= font)
nothing2.grid(row=3, column=0, sticky='wens')
after = tk.Label(frame2, text= "변경 후 ", relief="solid", font = font)
after.grid(row=3, column=1, columnspan=9, sticky='wens')
strX2 = tk.Label(frame2, text= "X값 ", width=4, relief="solid", font = font)
strX2.grid(row=4, column=0, sticky='wens')

X12 = tk.Label(frame2, text='-20', width=4, relief='solid', font=font)
X22 =tk.Label(frame2, text='-15', width=4, relief='solid', font=font)
X32 =tk.Label(frame2, text='-10', width=4, relief='solid', font=font)
X42 = tk.Label(frame2, text='-5', width=4, relief='solid', font=font)
X52 =tk.Label(frame2, text='0', width=4, relief='solid', font=font)
X62 = tk.Label(frame2, text='5', width=4, relief='solid', font=font)
X72 = tk.Label(frame2, text='10', width=4, relief='solid', font=font)
X82 = tk.Label(frame2, text='15', width=4, relief='solid', font=font)
X92 =tk.Label(frame2, text='20', width=4, relief='solid', font=font)

X12.grid(row=4, column=1, sticky='wens')
X22.grid(row=4, column=2, sticky='wens')
X32.grid(row=4, column=3, sticky='wens')
X42.grid(row=4, column=4, sticky='wens')
X52.grid(row=4, column=5, sticky='wens')
X62.grid(row=4, column=6, sticky='wens')
X72.grid(row=4, column=7, sticky='wens')
X82.grid(row=4, column=8, sticky='wens')
X92.grid(row=4, column=9, sticky='wens')

strY2 =tk.Label(frame2, text = 'Y값', width=4, relief="solid", font= font)
Y12 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y22 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y32 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y42 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y52 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y62 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y72 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y82 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)
Y92 = tk.Label(frame2, text = '', width=4, relief="solid", font= font)

strY2.grid(row=5, column=0, sticky='wens')
Y12.grid(row=5, column=1, sticky='wens')
Y22.grid(row=5, column=2, sticky='wens')
Y32.grid(row=5, column=3, sticky='wens')
Y42.grid(row=5, column=4, sticky='wens')
Y52.grid(row=5, column=5, sticky='wens')
Y62.grid(row=5, column=6, sticky='wens')
Y72.grid(row=5, column=7, sticky='wens')
Y82.grid(row=5, column=8, sticky='wens')
Y92.grid(row=5, column=9, sticky='wens')

window.mainloop()