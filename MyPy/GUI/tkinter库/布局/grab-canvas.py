from tkinter import *
from PIL import ImageGrab

width = 400
height = 300

def getter(widget):
    widget.update()
    print(root.winfo_rootx(), widget.winfo_x())  # 相对屏幕，相对窗口
    print(root.winfo_rooty(), widget.winfo_y())
    print(widget.winfo_width(), widget.winfo_height())  # 组件宽、高
    x = root.winfo_rootx() + widget.winfo_x()
    y = root.winfo_rooty() + widget.winfo_y()
    x1 = x + widget.winfo_width()
    y1 = y + widget.winfo_height()
    ImageGrab.grab().crop((x, y, x1, y1)).save("first.jpg")  # 为什么左上角坐标似乎到了窗口外面？

root = Tk()
cv = Canvas(root, width=width, height=height, bg='white')
cv.pack()

cv.create_rectangle(10, 10, 50, 50)
cv.create_line([0, 10, 100, 100], fill='green')
getter(cv)

root.mainloop()