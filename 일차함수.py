import tkinter as tk

window = tk.Tk()
window.title("일차함수")
window.geometry("400x400")
window.configure(bg='DarkTurquoise')
entry = tk.Entry(window)
entry.place(x=90, y=50)
def get_entry_value():
    print(entry.get())
button = tk.Button(window, text="입력", command=get_entry_value)
button.place(x=40, y=50)


window.mainloop()
