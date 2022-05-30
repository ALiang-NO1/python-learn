from turtle import *

for i in range(3, 10):
    circle(100, steps=i)
    home()
rt(90)    # 右转90度
pu()    # 抬笔
fd(30)    # 向前移动30px
write("Oh it's so cool!", align='center', font='王羲之书法字体')
hideturtle()
mainloop()