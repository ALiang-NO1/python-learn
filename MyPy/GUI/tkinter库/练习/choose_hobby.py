from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.codeHobby = IntVar()
        self.videoHobby = IntVar()
        print(self.codeHobby.get())
        self.c1 = Checkbutton(root, text="敲代码", variable=self.codeHobby, onvalue=1, offvalue=0)
        self.c2 = Checkbutton(root, text="看视频", variable=self.videoHobby, onvalue=1, offvalue=0)
        self.c1.pack(side='left')
        self.c2.pack(side='left')

        Button(root, text="确定", command=self.confirm).pack(side='left')
        Button(root, text='取消', command=root.quit).pack(side='left')

    def confirm(self):
        if self.videoHobby.get() == 1 and self.codeHobby.get() == 1:
            messagebox.showinfo("警告！", "请选择一门爱好！！！")
        elif self.videoHobby.get() == 0 and self.codeHobby.get() == 0:
            messagebox.showinfo("警告！", "请至少选择一门爱好!!!")
        else:
            if self.videoHobby.get() == 1:
                messagebox.showinfo("请选择你的爱好", "看视频都是正常人的爱好！你喜欢什么样的类型？")
            elif self.codeHobby.get() == 1:
                messagebox.showinfo("请选择你的爱好", "抓获野生程序猿一只，赶紧送他尚学堂的视频充饥！")

if __name__ == '__main__':
    root = Tk()
    root.title("爱好选择器")
    root.geometry('250x100-100+100')
    app = Application(master=root)
    root.mainloop()