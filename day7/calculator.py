from tkinter import *

root = Tk()
root.title("calculator")
root.geometry("240x260")

calc = Entry(root)
calc.grid(row = 0, column = 0, columnspan=3)

Button(text="1", bd = 2, command=lambda : add_digit(1)).grid(row = 1, column=0, stick = 'wens', padx = 2, pady = 2)
Button(text="2", bd = 2, command=lambda : add_digit(2)).grid(row = 1, column=1, stick = 'wens', padx = 2, pady = 2)
Button(text="3", bd = 2, command=lambda : add_digit(3)).grid(row = 1, column=2, stick = 'wens', padx = 2, pady = 2)
Button(text="4", bd = 2, command=lambda : add_digit(4)).grid(row = 2, column=0, stick = 'wens', padx = 2, pady = 2)
Button(text="5", bd = 2, command=lambda : add_digit(5)).grid(row = 2, column=1, stick = 'wens', padx = 2, pady = 2)
Button(text="6", bd = 2, command=lambda : add_digit(6)).grid(row = 2, column=2, stick = 'wens', padx = 2, pady = 2)
Button(text="7", bd = 2, command=lambda : add_digit(7)).grid(row = 3, column=0, stick = 'wens', padx = 2, pady = 2)
Button(text="8", bd = 2, command=lambda : add_digit(8)).grid(row = 3, column=1, stick = 'wens', padx = 2, pady = 2)
Button(text="9", bd = 2, command=lambda : add_digit(9)).grid(row = 3, column=2, stick = 'wens', padx = 2, pady = 2)
Button(text="0", bd = 2, command=lambda : add_digit(0)).grid(row = 4, column=1, stick = 'wens', padx = 2, pady = 2)

root.grid_columnconfigure(0,minsize = 60)
root.grid_columnconfigure(1,minsize = 60)
root.grid_columnconfigure(2,minsize = 60)

root.grid_rowconfigure(1,minsize = 60)
root.grid_rowconfigure(2,minsize = 60)
root.grid_rowconfigure(3,minsize = 60)
root.grid_rowconfigure(4,minsize = 60)

root.mainloop()