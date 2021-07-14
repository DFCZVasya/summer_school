from tkinter import *
import random

game_width = 500
game_height = 500

snake_item = 10

snake_color1 = "red"
snake_color2 = "yellow"

snake_x = 24
snake_y = 24

snake_x_nav = 0
snake_y_nav = 0

snake_list = []
snake_size = 3

presents_list = []
presents_size = 15

root = Tk()
root.title("Snake v1.0")

root.resizable(0,0)
canvas = Canvas(root, width=game_width, height=game_height)
canvas.pack()

for i in range(presents_size):
    x = temp_x = random.randint(0,49)
    y = temp_y = random.randint(0,49)
    id1 = canvas.create_oval(x*snake_item, y*snake_item,
                             x*snake_item + snake_item, 
                             y*snake_item+snake_item,
                             fill = "black")
    
    id2 = canvas.create_oval(x*snake_item + 2, y*snake_item + 2,
                             x*snake_item + snake_item - 2, 
                             y*snake_item+snake_item - 2,
                             fill = "blue")
    presents_list.append([temp_x, temp_y, id1, id2])

root.update()

def snake_print_item(canvas, x, y):
    global snake_list
    id1 = canvas.create_rectangle(x*snake_item, y*snake_item,
                             x*snake_item + snake_item, 
                             y*snake_item+snake_item,
                             fill = snake_color2)
    
    id2 = canvas.create_rectangle(x*snake_item + 2, y*snake_item + 2,
                             x*snake_item + snake_item - 2, 
                             y*snake_item+snake_item - 2,
                             fill = snake_color1)
    snake_list.append([x,y,id1,id2])
    if len(snake_list) > snake_size:
        tmp_item = snake_list.pop(0)
        canvas.delete(tmp_item[2])
        canvas.delete(tmp_item[3])

def check_if_present(x, y):
    global snake_size
    global presents_list
    for i in range(len(presents_list)):
        if presents_list[i][0] == x and presents_list[i][1] == y:
            canvas.delete(presents_list[2])
            canvas.delete(presents_list[3])
            snake_size += 1
            presents_list.pop(i)
            return

snake_print_item(canvas, snake_x, snake_y)

def snake_move(event):
    global snake_x
    global snake_y
    if event.keysym == "Up":
        snake_x_nav = 0
        snake_y_nav = -1
    elif event.keysym == "Down":
        snake_x_nav = 0
        snake_y_nav = 1
    elif event.keysym == "Left":
        snake_x_nav = -1
        snake_y_nav = 0
    elif event.keysym == "Right":
        snake_x_nav = 1
        snake_y_nav = 0
    snake_x  += snake_x_nav
    snake_y  += snake_y_nav
    snake_print_item(canvas, snake_x, snake_y)
    check_if_present(snake_x, snake_y)

canvas.bind_all("<KeyPress-Left>", snake_move)
canvas.bind_all("<KeyPress-Right>", snake_move)
canvas.bind_all("<KeyPress-Up>", snake_move)
canvas.bind_all("<KeyPress-Down>", snake_move)

root.mainloop()