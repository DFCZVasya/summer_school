from tkinter import *

def add_digit(digit):
    value = calc.get() + str(digit)
    calc.delete(0, END)
    calc.insert(0, value)

root = Tk()
root.title("calculator")
root.geometry("240x260")

calc = Entry(root, justify=RIGHT, font = ('Arial', 15), width= 15)
calc.grid(row = 0, column = 0, columnspan=3, stick = 'we')

Button(text="1", font = ('Arial', 20), bd = 2, command=lambda : add_digit(1)).grid(row = 1, column=0, stick = 'wens', padx = 2, pady = 2)
Button(text="2", font = ('Arial', 20), bd = 2, command=lambda : add_digit(2)).grid(row = 1, column=1, stick = 'wens', padx = 2, pady = 2)
Button(text="3", font = ('Arial', 20), bd = 2, command=lambda : add_digit(3)).grid(row = 1, column=2, stick = 'wens', padx = 2, pady = 2)
Button(text="4", font = ('Arial', 20), bd = 2, command=lambda : add_digit(4)).grid(row = 2, column=0, stick = 'wens', padx = 2, pady = 2)
Button(text="5", font = ('Arial', 20), bd = 2, command=lambda : add_digit(5)).grid(row = 2, column=1, stick = 'wens', padx = 2, pady = 2)
Button(text="6", font = ('Arial', 20), bd = 2, command=lambda : add_digit(6)).grid(row = 2, column=2, stick = 'wens', padx = 2, pady = 2)
Button(text="7", font = ('Arial', 20), bd = 2, command=lambda : add_digit(7)).grid(row = 3, column=0, stick = 'wens', padx = 2, pady = 2)
Button(text="8", font = ('Arial', 20), bd = 2, command=lambda : add_digit(8)).grid(row = 3, column=1, stick = 'wens', padx = 2, pady = 2)
Button(text="9", font = ('Arial', 20), bd = 2, command=lambda : add_digit(9)).grid(row = 3, column=2, stick = 'wens', padx = 2, pady = 2)
Button(text="0", font = ('Arial', 20), bd = 2, command=lambda : add_digit(0)).grid(row = 4, column=1, stick = 'wens', padx = 2, pady = 2)

root.grid_columnconfigure(0,minsize = 60)
root.grid_columnconfigure(1,minsize = 60)
root.grid_columnconfigure(2,minsize = 60)

root.grid_rowconfigure(1,minsize = 60)
root.grid_rowconfigure(2,minsize = 60)
root.grid_rowconfigure(3,minsize = 60)
root.grid_rowconfigure(4,minsize = 60)

root.mainloop()