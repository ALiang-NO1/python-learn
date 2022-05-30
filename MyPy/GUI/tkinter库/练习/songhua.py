"""测试一个经典的GUI写法，使用面向对象方式 """

from tkinter import *
from tkinter import messagebox

class Application(Frame):
    """一个经典GUI写法"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建组件"""
        self.btn01 = Button(self)
        self.btn01['text'] = '点击送花'
        self.btn01['command'] = self.songhua
        self.btn01.pack()
        # 创建一个退出按钮
        self.btnQuit = Button(self, text='退出', command=root.quit)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("送花", "送你99朵玫瑰花！")
        print("送花送花成功！")

root = Tk()
root.geometry('400x100-100+100')
root.title('一个经典的GUI程序类的测试')
app = Application(master=root)

root.mainloop()