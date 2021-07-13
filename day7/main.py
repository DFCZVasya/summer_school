from tkinter import *

clicks = 0

def btn_click():
    global clicks
    clicks += 1
    lable_text.set("Clicks: {}".format(clicks))
    

root = Tk()
root.title("new program on python!")
root.geometry("500x500")


lable_text = StringVar()
lable_text.set("Clicks: {}".format(clicks))

btn = Button(text="click me!", command=btn_click)
btn.place(relx = .5, rely = .5, anchor="c", height= 30, width=130)

lable = Label(textvariable=lable_text)
lable.place(relx = .5, rely = .1, anchor="c", height= 30, width=130)

root.mainloop()