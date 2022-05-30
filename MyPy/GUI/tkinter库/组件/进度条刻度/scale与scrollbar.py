# coding:utf-8
import tkinter  # 引入界面设计库

class MainForm:
    def __init__(self):
        self.root = tkinter.Tk()  # 新建一个窗体
        self.root.title("scrollbar测试：")  # 标题
        self.root.geometry("400x470-0+0")  # 初始窗口大小，为小写x
        self.root.maxsize(1000, 1000)  # 最大化后窗口大小
        # self.root.iconbitmap('ico.bmp')   # 图标，bmp格式可直接修改后缀
        self.root["background"] = "green"  # 界面颜色设置，其他颜色可以百度

        self.label = tkinter.Label(self.root, text="文字大小", fg="black", font=("微软雅黑", 10))
        self.label.pack(anchor="n")
        # scale组件
        self.scale = tkinter.Scale(self.root, label="拖动调整文字大小",
                                   from_=10, to=50, length=400,  # 设置标志大小和长度
                                   orient=tkinter.HORIZONTAL, showvalue=True,  # 设置水平放置
                                   tickinterval=10, resolution=True)  # 设置间隔、小数
        self.scale.bind("<B1-Motion>", self.change_value_handle)
        self.scale.pack(anchor="center")

        self.creat_widget()
        self.root.mainloop()

    # 改变字体大小
    def change_value_handle(self, event):
        self.label.config(font=("微软雅黑", self.scale.get()))
        self.listbox.config(font=("微软雅黑", self.scale.get()))
        self.show_label.config(font=("微软雅黑", self.scale.get()))

    # 创建一个widget
    def creat_widget(self):
        # 加一个标签
        self.widget_label = tkinter.Label(self.root, text="你想浏览的网站", fg="black", font=("微软雅黑", 10))
        self.widget_label.pack(anchor="s")

        # scrollbar是一个组件，包含两个部分：一个是listbox，一个是scrollbar
        self.frame = tkinter.Frame(self.root)
        self.listbox = tkinter.Listbox(self.frame, width=50, height=10)
        # 设置list内容
        for item in range(1, 101):
            self.listbox.insert("end", "[{info:0>3}]www.baidu.com".format(info=item))
        # 绑定事件
        self.listbox.bind("<Double-Button-1>", self.change_item_handle)
        # 设置滚动条
        self.scrollbar = tkinter.Scrollbar(self.frame)
        self.scrollbar.config(command=self.listbox.yview)
        # 设置显示标签
        self.content = tkinter.StringVar()
        self.content.set('empty')
        self.show_label = tkinter.Label(self.root, width=30, height=6, textvariable=self.content,
                                        bg='beige', fg="black", font=("微软雅黑", 10))

        self.scrollbar.pack(side="right", fill="y")
        self.listbox.pack(side="left")
        self.show_label.pack()
        self.frame.pack()

    def change_item_handle(self, event):
        item = "\n" + self.listbox.get(self.listbox.curselection())
        self.content.set(self.content.get() + item)  # 这样可以执行多选操作，item只是当前的选项，self.content是之前的选项
MainForm()