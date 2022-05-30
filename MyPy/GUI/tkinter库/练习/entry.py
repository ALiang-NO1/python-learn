from tkinter import *


def butonck():
    print(entryx.get())  # 输出输入框值


# 创建窗口
rview = Tk()
# 标题
rview.title("搞输入框")
# 窗口大小 长高用小写x隔开
rview.geometry("600x300-100+100")
# 创建lab标签
labelx = Label(rview, text="输入:", fg="red", font=("宋体", 30))
# 显示lab标签 网格布局 sticky=W #左对齐 E为右对齐 默认为中间对齐
labelx.grid(row=0, column=0)
# 创建输入框默认显示
entext = StringVar()
# 创建输入框
entryx = Entry(rview, font=("宋体", 20), textvariable=entext)
# 显示输入框
entryx.grid(row=0, column=1)
# 创建按钮
buttonx = Button(rview, text="确定", font=("宋体", 30), command=butonck)
# 显示按钮
buttonx.grid(row=0, column=2)

# -------------------------------------------------
# 设置内容
entext.set('西')
# 插入内容，最开始处
entryx.insert(0, '东')
# 插入内容，光标位置开始
entryx.insert(INSERT, '想')
# 插入内容，末尾
entryx.insert(END, '想')
# --------------------------------------------------

# 消息循环 显示窗口
rview.mainloop()
