from turtle import *

def draw_star1():
    fillcolor('red')
    begin_fill()
    while True:
        fd(200)
        right(144)
        if abs(pos()) < 1:
            break
    end_fill()
    mainloop()

def draw_star():
    setup(500, 500, -100, 200)
    pu()
    goto(-140, 80)
    pd()
    for i in range(5):
        fd(300)
        right(144)
    hideturtle()
    mainloop()

draw_star()