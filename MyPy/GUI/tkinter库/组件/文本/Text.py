from tkinter import Tk, Frame, Text, INSERT, END, Button, PhotoImage, Scrollbar
import webbrowser
import hashlib

class Application(Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.text = Text(root, width=40, height=6, font='楷体', fg='purple', bg='plum', bd=4)
        self.text.pack()
        self.text.insert(1.0, '0123456789\nabcdefghi')
        # 获取文本内容并转为哈希值
        self.contents = self.text.get('1.0', END)
        self.sig = self.getSig(self.contents)
        Button(self, text="插入文本", command=self.insertText).pack(side='left')
        Button(self, text="返回文本", command=self.returnText).pack(side='left')
        Button(self, text="添加图片", command=self.addImage).pack(side='left')
        Button(self, text="光标处添加组件", command=self.addWidget).pack(side='left')
        Button(self, text="通过tag精准控制文本", command=self.textTag).pack(side='left')
        Button(root, text="检查", command=self.check).pack()

    def insertText(self):
        self.text.insert(INSERT, "（光标处）")
        self.text.insert(END, "（末尾）")
        self.text.mark_set('here', 2.9)
        self.text.insert('here', "（mark-2.9）")

    def returnText(self):
        print(self.text.get(1.2, 1.6))
        self.text.insert(1.8, "（1.8）")
        print("所有文本内容：\n"+self.text.get(1.0, END))

    def addImage(self):
        # global photo
        self.image = PhotoImage(file='..\pic.gif')
        self.text.image_create(END, image=self.image)

    def addWidget(self):
        b1 = Button(self.text, text="爱尚学堂")
        self.text.window_create(INSERT, window=b1)

    def textTag(self):
        self.text.delete(1.0, END)
        self.text.insert(INSERT, "0123456789aaaa\n在这里插入标签\n已经清空所有内容\n测试代码是否生效\n百度")
        # Tags通常用于改变Text组件中内容的样式和功能，你可以修改文本的字体，尺寸和颜色，另外Tags还允许你将文本、嵌入的组件和图片与键盘相关联，
        # 除了user-defined tags(用户自定义的Tags)，还有一个预定义的特殊Tag：SEL
        self.text.tag_add('good', 1.0, 1.6)
        self.text.tag_config('good', background='yellow', foreground='blue')
        # 新的tag会覆盖旧的tag
        self.text.tag_add('bad', 1.3, 1.6)    # 设置标签属性
        self.text.tag_config('bad', background='silver', foreground='green')
        self.text.tag_add("link", 5.0, 5.2)
        self.text.tag_config("link", underline=True, foreground='red')
        # 绑定事件
        self.text.tag_bind('link', '<Enter>', self.show_arrow_cursor)
        self.text.tag_bind('link', '<Leave>', self.show_xterm_cursor)
        self.text.bind("link", '<Button-1>', self.webShow)

    def getSig(self, contents):
        m = hashlib.md5(contents.encode())
        return m.digest()

    def check(self):
        contents = self.text.get('1.0', END)
        if self.sig != self.getSig(contents):
            print('警报,内容发生改变')
        else:
            print('风平浪静')

    def show_arrow_cursor(self, event):
        self.text.config(cursor='arrow')

    def show_xterm_cursor(self, event):
        self.text.config(cursor='xterm')

    def webShow(self, event):
        webbrowser.open('http://www.baidu.com')

if __name__ == '__main__':
    root = Tk()
    root.geometry('400x200-100+100')
    app = Application(master=root)
    root.mainloop()

# 单击鼠标左键：<Button-1> #其中1为鼠标左键，2为鼠标右键，3为鼠标中键
# 左键移动：<B1-Motion>
# 左键释放：<ButtonRelease-1>
# 双击左键：<Double-Button-1>
# 进入：<Enter>
# 离开：<Leave>
# 获得光标:<FocusIn>
# 光标离开：<FoucusOut>
# 回车键：<Return>(F1,F2,F3,Delete…)
# 按任意键：<Key>
# ----------mark---------------
# 1.arks(标记)通常是嵌入到Text组件文本中的不可见的对象。事实上，Marks是指定字符间的位置，并跟随相应的字符一起移动。
# Marks有INSERT, CURRENT, 和user - defined
# 2.其中，INSERT和CURRENT是Tkinter预定义的特殊Marks，它们是不可能被删除的
# INSERT（或insert）用于指定当前插入光标的位置，Tkinter会在该位置绘制一个闪烁的光标（因此并不是所有的Marks都不可见）
# CURRENT用于指定与鼠标坐标坐标最近最接近的位置，不过，如果你按紧鼠标任何一个按钮，它会直到你松开它才响应
# 4.使用mark_set()方法创建和移动Marks
# 5.使用mark_unset()方法删除Marks
# 6.Mark事实上就是索引，用于表示位置