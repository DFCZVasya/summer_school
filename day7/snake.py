from tkinter import *

game_width = 500
game_height = 500

snake_item = 10

snake_color1 = "red"
snake_color2 = "yellow"

root = Tk()
root.title("Snake v1.0")

root.resizable(0,0)

canvas = Canvas(root, width=game_width, height=game_height)
canvas.pack()
root.update()

def snake_print_item(canvas, x, y):
    canvas.create_rectangle(x*snake_item, y*snake_item,
                             x*snake_item + snake_item, 
                             y*snake_item+snake_item,
                             fill = snake_color2)
    
    canvas.create_rectangle(x*snake_item + 2, y*snake_item + 2,
                             x*snake_item + snake_item - 2, 
                             y*snake_item+snake_item - 2,
                             fill = snake_color1)


root.mainloop()