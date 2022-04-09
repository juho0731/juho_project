from tkinter import *

from tkinter.ttk import*

from calc import*
root = Tk()
root.title('Test program')
root.geometry('395x400')

frm = Frame(root)

frm.pack(expand=True)

ent_expr = Entry(frm, font='맑은고딕 15')

ent_expr.grid(column=0, row=0, columnspan=4, sticky='wens')


btn1 = Button(frm, text='7')
btn1.grid(column=0, row=1, padx=5, pady=5, sticky='wens')
btn2 = Button(frm, text='8')
btn2.grid(column=1, row=1, padx=5, pady=5, sticky='wens')
btn3 = Button(frm, text='9')
btn3.grid(column=2, row=1, padx=5, pady=5, sticky='wens')
btn4 = Button(frm, text='+')
btn4.grid(column=3, row=1, padx=5, pady=5, sticky='wens')


btn5 = Button(frm, text='4')
btn5.grid(column=0, row=2, padx=5, pady=5, sticky='wens')
btn6 = Button(frm, text='5')
btn6.grid(column=1, row=2, padx=5, pady=5, sticky='wens')
btn7 = Button(frm, text='6')
btn7.grid(column=2, row=2, padx=5, pady=5, sticky='wens')
btn8 = Button(frm, text='-')
btn8.grid(column=3, row=2, padx=5, pady=5, sticky='wens')

btn9 = Button(frm, text='1')
btn9.grid(column=0, row=3, padx=5, pady=5, sticky='wens')
btn10 = Button(frm, text='2')
btn10.grid(column=1, row=3, padx=5, pady=5, sticky='wens')
btn11 = Button(frm, text='3')
btn11.grid(column=2, row=3, padx=5, pady=5, sticky='wens')
btn12 = Button(frm, text='*')
btn12.grid(column=3, row=3, padx=5, pady=5, sticky='wens')

btn13 = Button(frm, text='del')
btn13.grid(column=0, row=4, padx=5, pady=5, sticky='wens')
btn14 = Button(frm, text='0')
btn14.grid(column=1, row=4, padx=5, pady=5, sticky='wens')
btn15 = Button(frm, text='=')
btn15.grid(column=2, row=4, padx=5, pady=5, sticky='wens')
btn16 = Button(frm, text='/')
btn16.grid(column=3, row=4, padx=5, pady=5, sticky='wens')

def input_expr(txt: str):
    expr = ent_expr.get()       #Entry의 수식을 가져옴
    if len(expr) > 0 and expr[-1] in ('+','-','*','/') and txt in ('+','-','*','/'):
        lexpr = list(expr)
        lexpr[-1] = txt
        expr = ''.join(lexpr)
    elif len(expr) == 0 and txt in ('+', '-'):
        expr += '0' + txt
    else:
        expr += txt

    ent_expr.delete(0, 'end')   #Entry의 기존 수식을 전부 지움
    ent_expr.insert(0, expr)    #새로운 수식을 Entry에 넣어줌

#계산한 결과 갑을 ent에 출력하는 함수
def get_result():
    expr = ent_expr.get()
    if len(expr) == 0:
        return
    if expr[-1] in ('+','-','*','/'):
        expr = expr[:-1]
    calc = InCalc()
    calc.set_expression(expr)
    result = calc.evalution()
    ent_expr.delete(0, 'end')
    ent_expr.insert(0, str(result))


btn1.configure(command=lambda: input_expr('7'))
btn2.configure(command=lambda: input_expr('8'))
btn3.configure(command=lambda: input_expr('9'))
btn4.configure(command=lambda: input_expr('+'))
btn5.configure(command=lambda: input_expr('4'))
btn6.configure(command=lambda: input_expr('5'))
btn7.configure(command=lambda: input_expr('6'))
btn8.configure(command=lambda: input_expr('-'))
btn9.configure(command=lambda: input_expr('1'))
btn10.configure(command=lambda: input_expr('2'))
btn11.configure(command=lambda: input_expr('3'))
btn12.configure(command=lambda: input_expr('*'))
btn13.configure(command=lambda: ent_expr.delete(0, 'end'))
btn14.configure(command=lambda: input_expr('0'))
btn15.configure(command=get_result)
btn16.configure(command=lambda: input_expr('/'))

root.mainloop()

