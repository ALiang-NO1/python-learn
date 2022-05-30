import threading
import cv2
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()
root.title("东小东")

# 创建lab标签
label = Label(root, text="东小东TK视频流", fg="red", font=("宋体",30))
label.grid(row=0, column=0)

# 创建一个画布
canvas = Canvas(root, width=640, height=480, bg='red')
canvas.grid(row=1, column=0)

def show_video():
    global labelvvv
    vix = cv2.VideoCapture(2)  # 打开摄像头
    # imgtk=''
    while True:
        ret, tu = vix.read()  # ret为返回值，tu为当前帧
        tu1 = cv2.flip(tu, 1)    # 图像反转，1为左右对换，-1为上下对换
        cv2image = cv2.cvtColor(tu1, cv2.COLOR_BGR2RGBA)    # 转换颜色从BGR到
        current_image = Image.fromarray(cv2image)  # 将图像转换成Image对象
        imgtk = ImageTk.PhotoImage(image=current_image)     # img
        canvas.create_image(0,0,anchor=NW,image=imgtk)    # 将图片添加到画布
        obr = imgtk

# 开启线程
t1 = threading.Thread(target=show_video,args=())
t1.start()

root.mainloop()
