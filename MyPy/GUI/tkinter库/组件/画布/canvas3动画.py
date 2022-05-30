from tkinter import Tk, Canvas, Button
from time import sleep
from random import randint

root = Tk()
root.title('画布测试')
root.geometry('640x480-100+100')

canvas = Canvas(root, width=640, height=480, bg='lightgreen')
canvas.pack(fill='both', expand=True)

canvas.create_oval(30, 30, 80, 80, fill='yellow', outline='lightgrey')
canvas.create_oval(30, 100, 80, 150, fill='aqua', outline='lightgrey')
oval = canvas.create_oval(30, 200, 80, 250, fill='red', outline='brown')

def move():
    for i in range(46):
        if randint(1, 100) > 70:
            canvas.move(1, 5, 0)
        else:
            canvas.move(2, 5, 0)
        root.update()
        sleep(.05)

def move2(event):
    if event.keysym == 'Left':
        canvas.move(oval, -5, 0)
    if event.keysym == 'Down':
        canvas.move(oval, 0, 5)
    if event.keysym == 'Right':
        canvas.move(oval, 5, 0)
    if event.keysym == 'Up':
        canvas.move(oval, 0, -5)

canvas.bind_all('<KeyPress-Left>', move2)
canvas.bind_all('<KeyPress-Right>', move2)
canvas.bind_all('<KeyPress-Down>', move2)
canvas.bind_all('<KeyPress-Up>', move2)

Button(canvas, text='开始', command=move).pack(anchor='s')
root.mainloop()
