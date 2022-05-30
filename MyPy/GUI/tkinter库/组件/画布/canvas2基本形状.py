"""画布实现绘制弧、（椭）圆、线条、矩形的绘制"""
from tkinter import Tk, Canvas
from random import randint
from PIL import ImageTk, Image

root = Tk()
root.title('画布测试')
root.geometry('640x480-100+100')

canvas = Canvas(root, width=640, height=480, bg='lightgreen')
canvas.pack(fill='both', expand=True)

# 创建矩形
for i in range(3):
    x1, y1 = randint(1, 640), randint(1, 480)
    x2, y2 = randint(1, 640), randint(1, 480)
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        x1, x2 = x2, y2
    canvas.create_rectangle(x1, y1, x2, y2)

canvas.create_oval(10, 10, 11, 11, fill='red')  # 圆左上角
canvas.create_arc(10, 10, 110, 110, extent=359, style='arc')  # 圆
canvas.create_oval(110, 110, 111, 111, fill='red')  # 右下角

canvas.create_arc(210, 10, 310, 110, extent=180, style='chord', fill='yellow')

canvas.create_arc(10, 250, 310, 350, extent=180, style='arc')  # 不闭合没有填充

canvas.create_oval(320, 250, 321, 251, fill='red')  # 左上角
canvas.create_arc(320, 250, 620, 350, extent=270, style='arc')  # 椭圆
canvas.create_oval(620, 350, 621, 351, fill='red')  # 右下角

file = Image.open(r'..\pic.gif')
img = ImageTk.PhotoImage(file)
id = canvas.create_image(30, 330, anchor='nw', image=img)
print(canvas.coords(id))


def draw(event):  # 拖拽绘制线条
    x1, y1 = event.x, event.y
    x2, y2 = event.x, event.y
    canvas.create_oval(x1, y1, x2+1, y2+1, fill='red')

canvas.bind('<B1-Motion>', draw)

root.mainloop()
