from tkinter import *

root = Tk()

canvas = Canvas(root, width=500, height=500)

canvas.pack()

shreck_obj = PhotoImage(file="shreck.png")
canvas.create_image(50,50, anchor = NW, image = shreck_obj)
root.mainloop()