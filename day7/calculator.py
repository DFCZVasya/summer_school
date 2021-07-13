from tkinter import *

def add_digit(digit):
    value = calc.get() + str(digit)
    calc.delete(0, END)
    calc.insert(0, value)

def make_digit_button(digit):
    return Button(text=str(digit), font = ('Arial', 20), bd = 2, command=lambda : add_digit(digit))

root = Tk()
root.title("calculator")
root.geometry("240x260")

calc = Entry(root, justify=RIGHT, font = ('Arial', 15), width= 15)
calc.grid(row = 0, column = 0, columnspan=3, stick = 'we')

make_digit_button(1).grid(row = 1, column=0, stick = 'wens', padx = 2, pady = 2)
make_digit_button(2).grid(row = 1, column=1, stick = 'wens', padx = 2, pady = 2)
make_digit_button(3).grid(row = 1, column=2, stick = 'wens', padx = 2, pady = 2)
make_digit_button(4).grid(row = 2, column=0, stick = 'wens', padx = 2, pady = 2)
make_digit_button(5).grid(row = 2, column=1, stick = 'wens', padx = 2, pady = 2)
make_digit_button(6).grid(row = 2, column=2, stick = 'wens', padx = 2, pady = 2)
make_digit_button(7).grid(row = 3, column=0, stick = 'wens', padx = 2, pady = 2)
make_digit_button(8).grid(row = 3, column=1, stick = 'wens', padx = 2, pady = 2)
make_digit_button(9).grid(row = 3, column=2, stick = 'wens', padx = 2, pady = 2)
make_digit_button(0).grid(row = 4, column=1, stick = 'wens', padx = 2, pady = 2)

root.grid_columnconfigure(0,minsize = 60)
root.grid_columnconfigure(1,minsize = 60)
root.grid_columnconfigure(2,minsize = 60)

root.grid_rowconfigure(1,minsize = 60)
root.grid_rowconfigure(2,minsize = 60)
root.grid_rowconfigure(3,minsize = 60)
root.grid_rowconfigure(4,minsize = 60)

root.mainloop()