from tkinter import Tk, Frame, Canvas, PhotoImage, Button
import random

class Application(Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """create.oval为绘制圆形，fill填充颜色。
           create.arc为绘制扇形，start和extent表示该扇形从0°到180°。"""
        self.canvas = Canvas(self, width=300, height=250, bg='peru')
        self.canvas.pack()
        self.canvas.create_line(20, 10, 30, 20, 80, 36, 90, 1)
        self.canvas.create_rectangle(50, 50, 100, 100)
        global photo
        photo = PhotoImage(file=r'..\..\src\pic.gif')
        self.canvas.create_image(150, 200, image=photo)
        Button(self, text="画5个矩形", command=self.draw5Rect).pack(side='left')

    def draw5Rect(self):
        for i in range(0, 5):
            x1 = random.randrange(int(self.canvas['width'])/2)
            y1 = random.randrange(int(self.canvas['height'])/2)
            x2 = x1 + random.randrange(int(self.canvas['width'])/2)
            y2 = y1 + random.randrange(int(self.canvas['width'])/2)
            self.canvas.create_rectangle(x1, y1, x2, y2)

if __name__ == '__main__':
    root = Tk()
    root.geometry('320x300-200+100')
    app = Application(master=root)
    root.mainloop()