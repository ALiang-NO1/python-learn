from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import re
import requests

def butonck():
    # 改变lab颜色
    label["fg"] = "green"
    # 获取输入框值
    name = entry.get()
    # 去掉字符串前后空格
    name = name.strip()
    if name == '':
        # 弹出提示框
        messagebox.showinfo("提示", "输入不可为空!")
    else:
        # fonts: 1.ttf（艺术签）  3.ttf（个性签）  8.ttf（商务签）  bzcs.ttf（潇洒签）
        #        2.ttf（行书签）  zql.ttf（连笔签）  ykq.ttf（可爱签）  lfc.ttf（草体签）
        data = {"word": name, "sizes": 60, "fonts": "lfc.ttf", "fontcolor": "# 000000"}   # 字典数据
        res = requests.post("http://www.uustv.com/", data=data)
        # res.encoding = "utf-8"
        html = res.text   # 网站源码
        zz = '<div class="tu">.*?<img src="(.*?)"/></div>'  # 括号里的.*?表示要取的值
        # 取图片地址<div class="tu">﻿<img src="tmp/160601377941345.gif"></div>
        suffix = re.findall(zz, html)
        # 取图片数据
        content = requests.get("http://www.uustv.com/"+suffix[0]).content
        # 打开文件
        ff = open('{}.gif'.format(name), "wb")
        # 写图片数据
        ff.write(content)
        ff.close()

        bmx = ImageTk.PhotoImage(file='{}.gif'.format(name))
        lab2 = Label(rview, image=bmx)
        lab2.bm = bmx
        lab2.grid(row=2, columnspan=2)
# 创建窗口
rview = Tk()
# 标题
rview.title("签名设计")
# 窗口大小 长高用小写x隔开
rview.geometry("-100+100")
# 窗口基于屏幕的坐标 +x轴+y轴
# rview.geometry("+500+200")
# 创建lab标签
label = Label(rview, text="签名", fg="red", font=("宋体", 30))
# 显示lab标签 网格布局 sticky = W # 左对齐 E为右对齐 默认为中间对齐
label.grid(row=0, column=0)
# 创建输入框
entry = Entry(rview, font=("宋体", 20))
# 显示输入框
entry.grid(row=0, column=1)
# 创建按钮
button = Button(rview, text="确定", font=("宋体", 30), command=butonck)
# 显示按钮
button.grid(row=1, column=2)
# 显示后改变按钮属性
# button["width"] = 2
# 消息循环 显示窗口
rview.mainloop()