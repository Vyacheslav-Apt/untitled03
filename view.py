import model
import tkinter as tk
window = tk.Tk()
import time


window.geometry("1300x700")
canvas = tk.Canvas(window, width=300, height=600, background="orange")


zvet = [model.siniy]     #цвет игрока

def draw():
    canvas.delete(tk.ALL)                      #рисует поле
    for i in range(10):
      for j in range(10):
        if i == model.dx and j == model.dy:      #рисует игрока
            color = model.siniy
            tag = "main"
        if i == model.maze[1] and j == model.maze[2]:                  #рисует квадраты, которые надо ловить
            color = model.maze[3]
            tag = "nemain"
        else:
            color = "red"
            tag = ""
        x = 60
        canvas.create_rectangle(i * x, j * x, i * x + x, j * x + x, fill=color, tag=tag) #рисует поле

time.sleep(1)               #таймер, позволяющий квадратам падать вниз
for i in range(1):
    model.dp = model.dp + 1

if model.dx == model.maze[1] and model.dy == model.maze[2] and zvet == model.maze[3]:  #это так называемые уровни, если координаты и цвет совпадают, то цвет игрока меняется
    zvet.clear()
    zvet.append([model.sheltyy])
else:
    print("Проигрыш")  #это условно, хочется, чтоб появлялось на экране игры
    if model.dx == model.maze[1] and model.dy == model.maze[2] and zvet == model.maze[3]: #это так называемые уровни, если координаты и цвет совпадают, то цвет игрока меняется
        zvet.clear()
        zvet.append([model.rozoviy])
    else:
        print("Проигрыш") #это условно, хочется, чтоб появлялось на экране игры

draw()

def go_left(event):
if model.dx > 0:
    model.dx -= 1
draw()


def go_right(event):
    if model.dx < 4:
        model.dx += 1
    draw()


window.bind("<a>", go_left)
window.bind("<d>", go_right)


canvas.pack()
window.mainloop()