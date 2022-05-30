from tkinter import Tk, Message

myWindow = Tk()    # 创建一个tk窗口
myWindow.title('GUI程序练习')    # 窗口大标题
myWindow.geometry('380x300-100+100')    # 窗口位置及位置

whatever_you_do = "只总\n要能\n用成\n心功\n   ！"
msg = Message(myWindow, text=whatever_you_do)
msg.config(bg='lightgreen', font=('王羲之书法字体', 20))
msg.pack()

# 空格表换行，单位像素
text = 'Message()方法的第一个参数是父对象，表示这个标签将建立在哪一个父对象内。 下列是Message()方法内其他常用的options参数。'
msg2 = Message(myWindow, text=text, bg='beige', aspect=200, width=300)
msg2.pack(pady=4)

myWindow.mainloop()