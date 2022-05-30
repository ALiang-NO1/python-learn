from tkinter import Tk, Canvas, Label
from math import sin, cos, pi

root = Tk()
root.title('画布测试')
root.geometry('400x300-100+100')

canvas = Canvas(root, bg='beige')
canvas.pack()
# 测试箭头arrow
canvas.create_line(5, 5, 100, 100, 150, 50, arrow='last', fill='red')
canvas.create_line(5, 150, 100, 22, arrow='first', fill='blue', dash=(5, 3))
# 测试端点处capstyle
canvas.create_line(130, 230, 320, 230, capstyle='round')
canvas.create_line(130, 240, 320, 240, width=10, capstyle='round')
canvas.create_line(130, 260, 320, 260, width=10, capstyle='projecting')
# 测试闭合处joinstyle
canvas.create_line(15, 180, 70, 150, 111, 180, 15, 180, width=20, joinstyle='round')
canvas.create_line(15, 230, 70, 200, 111, 230, 15, 230, width=20, joinstyle='bevel')
# canvas.create_line(15, 380, 70, 350, 111, 380, 15, 380, width=20, capstyle='butt', joinstyle='miter')

x_center, y_center, r = 240, 130, 100
x, y = [], []
for i in range(12):
    x.append(x_center + r*cos(30*i*pi/180))
    y.append(y_center + r*sin(30*i*pi/180))
for i in range(12):
    for j in range(12):
        canvas.create_line(x[i], y[i], x[j], y[j])

# 建一个能输出坐标的标签
def show_pos(e):
    label['text'] = str(e.x) + ' ' + str(e.y)

label = Label(root, bg='yellow', width=50, height=1)
label.pack()
canvas.bind('<Motion>', lambda e: show_pos(e))

root.mainloop()
