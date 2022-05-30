from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import *

class Application(Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建主菜单
        menubar = Menu(root)
        # 创建子菜单
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)
        # 将子菜单加入主菜单
        menubar.add_cascade(label="文件(F)", menu=menuFile)
        menubar.add_cascade(label="编辑(E)", menu=menuEdit)
        menubar.add_cascade(label="帮助(H)", menu=menuHelp)
        # 将主菜单栏加到根窗口
        root['menu'] = menubar
        # 添加菜单项
        menuFile.add_command(label="新建", accelerator='Ctr+N', command=self.newfile)
        menuFile.add_command(label="打开", accelerator='Ctr+O', command=self.openfile)
        menuFile.add_command(label="保存", accelerator='Ctr+N', command=self.savefile)
        menuFile.add_command(label="退出", accelerator="Ctr+Q", command=self.quit)
        menuFile.add_separator()  # 添加分割线
        # 增加快捷键
        root.bind('<Control-N>', lambda event: self.newfile())
        root.bind('<Control-O>', lambda event: self.openfile())
        root.bind('<Control-S>', lambda event: self.savefile())
        root.bind('<Control-Q>', lambda event: self.exit())
        # 文本编辑区
        self.textpad = Text(root, width=50, height=30)
        self.textpad.pack()
        # 创建上下菜单
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label="背景颜色", command=self.openAskcolor)
        # 为右键绑定事件
        root.bind('<Button-3>', self.createContextMenu)

    def newfile(self):
        # self.textpad.delete('1.0', 'end')   # 清空textpad中的所有控件
        self.filename = asksaveasfilename(title="另存为", initialfile="未命名.txt", defaultextension='.txt')
        self.savefile()

    def openfile(self):
        self.textpad.delete('1.0', 'end')
        with askopenfile(title="打开文本文档") as f:
            self.textpad.insert(INSERT, f.read())
            self.filename = f.name

    def savefile(self):
        with open(self.filename, 'w') as f:
            c = self.textpad.get(1.0, END)
            f.write(c)

    def exit(self):
        root.quit()

    def openAskcolor(self):
        s1 = askcolor(color='red', title="选择背景颜色")
        self.textpad.config(bg=s1[1])

    def createContextMenu(self, event):
        # 菜单在鼠标右键单击时显示
        self.contextMenu.post(event.x_root, event.y_root)

if __name__ == '__main__':
    root = Tk()
    root.geometry('500x400-100+100')
    app = Application(master=root)
    root.mainloop()