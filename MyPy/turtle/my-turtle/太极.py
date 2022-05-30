from turtle import *

clear()
up()    # 将画笔从画布上提起。即在画笔移动过程中不画出笔迹
setpos(0, -100)    # 将画笔移动到画布的这个位置
down()    # 将画笔放到画布上。即之后画笔的移动都会留下笔迹

# 画阴鱼
fillcolor("black")
begin_fill()
circle(100, 180)
end_fill()

# fillcolor("black")
begin_fill()
circle(50, 180)
end_fill()

fillcolor("white")
begin_fill()
circle(-50, 180)
end_fill()

# 画阳鱼
circle(-100, 180)

# 画阳眼
up()
setpos(0, 50-15)
down()
# fillcolor("white")
begin_fill()
circle(15)
end_fill()

# 画阴眼
up()
setpos(0, -50-15)
down()
fillcolor("black")
begin_fill()
circle(15)
end_fill()
mainloop()