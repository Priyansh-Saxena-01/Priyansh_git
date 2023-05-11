from tkinter import *

window = Tk()
window.resizable(0,0)
window.geometry("350x350")
window.title("Basic calculator")

input_val=StringVar()


def enter_backspace():
    global expression
    expression=input_field.get()
    expression=expression.rstrip(expression[-1])
    input_val.set(expression)

def enter_clear():
    global expression
    input_val.set("")
    expression=""

def enter_equal():
    global expression
    expression=input_field.get()
    input_val.set(str(eval(expression)))
    expression=""


def click(item):
    global expression
    expression=input_field.get()
    expression=expression+str(item)
    input_val.set(expression)

expression=""

input_frame=Frame(window,width=350,height=100,highlightbackground="red",highlightcolor="red",highlightthickness=3)
input_frame.pack(side=TOP)

input_field= Entry(input_frame,width=50,font=('jokerman',20,'bold'),fg='green',textvariable=input_val,justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

btn_frame=Frame(window,width=350,height=250,highlightbackground='black',highlightcolor='black',highlightthickness=0)
btn_frame.pack()


clear = Button(btn_frame, text = "Clear", fg = "green", width = 30, height = 3, bd=1, cursor = "hand2", command = lambda: enter_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

divide = Button(btn_frame, text = "/", fg = "black", width = 8, height = 3, bd=1, cursor = "hand2", command = lambda: click("/")).grid(row = 2, column = 3, padx = 1, pady = 1)

multiply= Button(btn_frame, text = "x", fg = "black", width = 8, height = 3, bd=1, cursor = "hand2", command = lambda: click("*")).grid(row = 2, column = 4,padx = 1, pady = 1)

one= Button(btn_frame, text = "1", fg = "black", width = 9, height = 3, bd=1, cursor = "hand2", command = lambda: click("1")).grid(row = 1, column = 0, padx = 1, pady = 1)

two= Button(btn_frame, text = "2", fg = "black", width = 9, height = 3, bd=1, cursor = "hand2", command = lambda: click("2")).grid(row = 1, column = 1, padx = 1, pady = 1)

three= Button(btn_frame, text = "3", fg = "black", width = 9, height = 3, bd=1, cursor = "hand2", command = lambda: click("3")).grid(row = 1, column = 2, padx = 1, pady = 1)

plus= Button(btn_frame, text = "+", fg = "black", width = 8, height = 3, bd=1, cursor = "hand2", command = lambda: click("+")).grid(row = 1, column = 3, padx = 1, pady = 1)

minus= Button(btn_frame, text = "-", fg = "black", width = 8, height = 3, bd=1, cursor = "hand2", command = lambda: click("-")).grid(row = 1, column = 4, padx = 1, pady = 1)

four= Button(btn_frame, text = "4", fg = "black", width = 9, height = 3, bd=1, cursor = "hand2", command = lambda: click("4")).grid(row = 2, column = 0, padx = 1, pady = 1)

five= Button(btn_frame, text = "5", fg = "black", width = 9, height = 3, bd=1, cursor = "hand2", command = lambda: click("5")).grid(row = 2, column = 1, padx = 1, pady = 1)

six= Button(btn_frame, text = "6", fg = "black", width = 9, height = 3, bd=1, cursor = "hand2", command = lambda: click("6")).grid(row = 2, column = 2, padx = 1, pady = 1)

dot= Button(btn_frame, text = ".", fg = "black", width = 8, height = 3, bd=1, cursor = "hand2", command = lambda: click(".")).grid(row = 4, column = 3, padx = 1, pady = 1)

remainder= Button(btn_frame, text = "%", fg = "black", width = 8, height = 3, bd=1, cursor = "hand2", command = lambda: click("%")).grid(row = 4, column = 4, padx = 1, pady = 1)

equals= Button(btn_frame, text = "=", fg = "black", width = 18, height = 3, bd=1, cursor = "hand2", command = lambda: enter_equal()).grid(row = 3, column = 3,columnspan=2, padx = 1, pady = 1)

hundred= Button(btn_frame, text = "100", fg = "black", width = 9, height = 3, bd=1, cursor = "hand2", command = lambda: click("00")).grid(row = 3, column = 0, padx = 1, pady = 1)

thousand= Button(btn_frame, text = "1000", fg = "black", width = 9, height = 3, bd=1, cursor = "hand2", command = lambda: click("000")).grid(row = 3, column = 1, padx = 1, pady = 1)

right_bracket= Button(btn_frame, text = "(", fg = "black", width = 9, height = 3, bd=1, cursor = "hand2", command = lambda: click("(")).grid(row = 4, column = 0, padx = 1, pady = 1)

left_bracket= Button(btn_frame, text = ")", fg = "black", width = 9, height = 3, bd=1, cursor = "hand2", command = lambda: click(")")).grid(row = 4, column = 1, padx = 1, pady = 1)

power= Button(btn_frame, text = "^", fg = "black", width = 9, height = 3, bd=1, cursor = "hand2", command = lambda: click("**")).grid(row = 4, column = 2, padx = 1, pady = 1)

backspace= Button(btn_frame, text = "Backspace", fg = "black", width = 18, height = 3, bd=1, cursor = "hand2", command = lambda: enter_backspace()).grid(row = 0, column = 3,columnspan=2, padx = 1, pady = 1)

zero= Button(btn_frame, text = "0", fg = "black", width = 9, height = 3, bd=1, cursor = "hand2", command = lambda: click("0")).grid(row = 3, column = 2, padx = 1, pady = 1)

window.mainloop()
