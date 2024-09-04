#Tkinter
from tkinter import *

calc = Tk()
calc.title("Calculator")
calc.iconbitmap("calculator.ico")
calc.config(bg = "#145087")
calc.resizable(0,0)

#when buttons clicked
def btn_clk(num):
    cur_num = db.get()
    clear()
    f_num = cur_num + num
    db.insert(0, f_num)

#global variable for using in many functions
first_num = 0
math = ""

#determine the type of operations
def cal(math_type):
    global first_num, math
    first_num = db.get()
    math = math_type
    clear()

#Arthematic operations
def equal():
    result = ""
    global first_num
    second_num = db.get()   
    clear()
    if math == "add":
       result = int(first_num) + int(second_num)
    elif math == "sub":
       result = int(first_num) - int(second_num)
    elif math == "mult":
       result = int(first_num) * int(second_num)
    elif math == "div":
       result = int(first_num) / int(second_num)
    else:
        result = "error"
    db.insert(0, result)

#clear the display
def clear():
    db.delete(0,END)

#display
db = Entry(calc, width = 14, font = ("Vardana",30), justify = "right", bg = "#8bdfe0")
db.grid(row = 0, column = 0, columnspan = 3)

#Buttons and their operations
btn_1 = Button(calc, text = "1", font = ("Comfortaa",14), padx = 38, pady = 10, bg = "#79b5ed", command = lambda: btn_clk("1"))
btn_1.grid(row = 3, column = 0)

btn_2 = Button(calc, text = "2", font = ("Comfortaa",14), padx = 38, pady = 10, bg = "#79b5ed", command = lambda: btn_clk("2"))
btn_2.grid(row = 3, column = 1)

btn_3 = Button(calc, text = "3", font = ("Comfortaa",14), padx = 38, pady = 10, bg = "#79b5ed", command = lambda: btn_clk("3"))
btn_3.grid(row = 3, column = 2)

btn_4 = Button(calc, text = "4", font = ("Comfortaa",14), padx = 38, pady = 10, bg = "#79b5ed", command = lambda: btn_clk("4"))
btn_4.grid(row = 2, column = 0)

btn_5 = Button(calc, text = "5", font = ("Comfortaa",14), padx = 38, pady = 10, bg = "#79b5ed", command = lambda: btn_clk("5"))
btn_5.grid(row = 2, column = 1)

btn_6 = Button(calc, text = "6", font = ("Comfortaa",14), padx = 38, pady = 10, bg = "#79b5ed", command = lambda: btn_clk("6"))
btn_6.grid(row = 2, column = 2)

btn_7 = Button(calc, text = "7", font = ("Comfortaa",14), padx = 38, pady = 10, bg = "#79b5ed", command = lambda: btn_clk("7"))
btn_7.grid(row = 1, column = 0)

btn_8 = Button(calc, text = "8", font = ("Comfortaa",14), padx = 38, pady = 10, bg = "#79b5ed", command = lambda: btn_clk("8"))
btn_8.grid(row = 1, column = 1)

btn_9 = Button(calc, text = "9", font = ("Comfortaa",14), padx = 38, pady = 10, bg = "#79b5ed", command = lambda: btn_clk("9"))
btn_9.grid(row = 1, column = 2)

btn_0 = Button(calc, text = "0", font = ("Comfortaa",14), padx = 38, pady = 10, bg = "#79b5ed", command = lambda: btn_clk("0"))
btn_0.grid(row = 4, column = 0)

btn_clear = Button(calc, text = "clear", font = ("Comfortaa",15), padx = 74, pady = 10, bg = "#79b5ed", command = clear)
btn_clear.grid(row = 4, column = 1, columnspan = 2)

btn_div = Button(calc, text = "/", font = ("Comfortaa",15), padx = 40, pady = 10, bg = "#79b5ed", command = lambda : cal('div'))
btn_div.grid(row = 5, column = 0)

btn_mult = Button(calc, text = "*", font = ("Comfortaa",14), padx = 40, pady = 10, bg = "#79b5ed", command =lambda : cal('mult'))
btn_mult.grid(row = 5, column = 1)

btn_equal = Button(calc, text = "=", font = ("Comfortaa",14), padx = 38, pady = 40, bg = "#79b5ed", command = equal)
btn_equal.grid(row = 5, column = 2, rowspan = 2)

btn_sub = Button(calc, text = "-", font = ("Comfortaa",14), padx = 40, pady = 10, bg = "#79b5ed", command = lambda : cal('sub'))
btn_sub.grid(row = 6, column = 0)

btn_add = Button(calc, text = "+", font = ("Comfortaa",14), padx = 38, pady = 10, bg = "#79b5ed", command = lambda : cal('add'))
btn_add.grid(row = 6, column = 1)

calc.mainloop()
