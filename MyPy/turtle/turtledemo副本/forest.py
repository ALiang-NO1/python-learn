from turtle import Turtle, colormode, tracer, mainloop
from random import randrange
from time import perf_counter as clock

"""
Description: 一枝干三分枝的树

Author: Erich Neuwirth
Logo项目：http://homepage.univie.ac.at/erich.neuwirth/

Modifier: ALiang（2021.4。30）
Csdn: https://blog.csdn.net/weixin_49012647
Wechat: 【全面资源集】
"""

def symRandom(n):  # 生产[-n, n]的随机数
    return randrange(-n, n+1)

def randomize(branchlist, angledist, sizedist):
    #       （[(45, 0.69), (0, 0.65), (-45, 0.71)],  10,  5）
    return [(angle+symRandom(angledist), 
             sizefactor*1.01**symRandom(sizedist)) for angle, sizefactor in branchlist]

def randomfd(t, distance, parts, angledist):  # 左转【0,10】度，前进80/5，循环5次
    #       (t, 80,       5,     10)
    for i in range(parts):
        t.left(symRandom(angledist))
        t.forward((1.0 * distance)/parts)

def tree(tlist, size, level, widthfactor, branchlists, angledist=10, sizedist=5):
    # turtle(), 80,   5,     0.1,         [[(45, 0.69), (0, 0.65), (-45, 0.71)]]
    # 一只龟：turtle() 对应一个列表：[[(45, 0.69), (0, 0.65), (-45, 0.71)]]
    if level > 0:
        lst = []
        brs = []
        for t, branchlist in list(zip(tlist, branchlists)):  # 龟，[(45, 0.69), (0, 0.65), (-45, 0.71)]
            t.pensize(size * widthfactor)
            t.pencolor(255 - (180 - 11 * level + symRandom(15)), 
                       180 - 11 * level + symRandom(15),
                       0)
            t.pendown()
            randomfd(t, size, level, angledist)
            yield 1
            for angle, sizefactor in branchlist:
                t.left(angle)
                lst.append(t.clone())
                brs.append(randomize(branchlist, angledist, sizedist))
                t.right(angle)
        for x in tree(lst, size*sizefactor, level-1, widthfactor, brs, 
                      angledist, sizedist):
            yield None


def start(t, x, y):  # 转90度，然后跳到（x,y），落笔
    colormode(255)  # 默认就是255，删？!
    t.reset()  # 是否清除颜色模式？上句有用？
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.penup()
    t.setpos(x, y)
    t.pendown()

def doit1(level, pen):
    pen.hideturtle()
    start(pen, 20, -208)
    t = tree([pen], 80, level, 0.1, [[(45, 0.69), (0, 0.65), (-45, 0.71)]])
    return t

def doit2(level, pen):
    pen.hideturtle()
    start(pen, -135, -130)
    t = tree([pen], 120, level, 0.1, [[(45, 0.69), (-45, 0.71)]])
    return t

def doit3(level, pen):
    pen.hideturtle()
    start(pen, 190, -90)
    t = tree([pen], 100, level, 0.1, [[(45, 0.7), (0, 0.72), (-45, 0.65)]])
    return t

# Hier 3 Baumgeneratoren:
def main():
    p = Turtle()
    p.ht()
    tracer(75, 0)
    u = doit1(6, Turtle(undobuffersize=1))
    s = doit2(7, Turtle(undobuffersize=1))
    t = doit3(5, Turtle(undobuffersize=1))
    a = clock()
    while True:
        done = 0
        for b in u, s, t:
            try:
                b.__next__()
            except:
                done += 1
        if done == 3:
            break

    tracer(1, 10)
    b = clock()
    return "runtime: %.2f sec." % (b-a)

if __name__ == '__main__':
    main()
    mainloop()
