from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        Label(self, text="用户名").grid(row=0, column=0)

        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.grid(row=0, column=1)
        v1.set('admin')

        Label(self, text="(用户名为手机号)", fg='red').grid(row=0, column=2)
        Label(self, text="密  码").grid(row=1, column=0)

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show='*')
        self.entry02.grid(row=1, column=1)

        Button(self, text="登入", command=self.login).grid(row=2, column=1, sticky=E)
        Button(self, text="取消", command=self.quit).grid(row=2, column=1, sticky=W)

    def login(self):
        username = self.entry01.get()
        psw = self.entry02.get()
        print("登入：正在与数据库比对用户名与密码.....")
        print("用户名："+username)
        print("密码："+psw)
        if username == 'liang' and psw == '123456':
            messagebox.showinfo("尚学堂学习系统！", "登入成功，开始学习。")
            print("-----正确-----")
        else:
            messagebox.showerror("尚学堂学习系统！", "登入失败，用户名或密码错误！！")
            print("-----错误-----")

root = Tk()
root.geometry('400x100-100+100')
root.title('通过网格控制登入界面')
app = Application(master=root)
root.mainloop()