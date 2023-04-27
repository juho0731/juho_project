import tkinter as tk

window = tk.Tk()
window.title("일차함수")
window.geometry("400x400")
entry = tk.Entry(window)
entry.place(x=50, y=50)
text1 = tk.Label(window, text="입력값")
text1.place(x=30, y=50)
window.mainloop()

