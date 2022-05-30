from tkinter import Tk, Label, CENTER, PhotoImage

myWindow = Tk()  # 创建一个tk窗口

a = int(myWindow.winfo_screenwidth())
b = int(myWindow.winfo_screenheight())
print(a, b)
rgb = myWindow.winfo_rgb('lightblue')
print(rgb[0]//255, rgb[1]//255, rgb[2]//255)

text = "“全面资源集”是一个提供优质资源及技术文章分享的公众号，应该得到推广。让更多人接受它的恩惠。"
Label(myWindow, text=text, background='khaki', foreground='coral', justify='left', padx=22, pady=16,
      font='楷体 14 bold', wraplength=200, width=24, height=4).pack()  # 或者font=('Helvetic',20,'bold')

logo = PhotoImage(file='../pic.gif')    # 传入gif图片
# Label(myWindow, image=logo).pack(side='left')    # 打包并调整位置,side可传:top, bottom, left, or right
explanation = """扑进春天的怀抱，亲近大自然。\n用心感受万物的温暖！"""    # 在图片上打字
Label(myWindow, compound=CENTER, text=explanation, font='方正舒体 18', fg='springgreen', image=logo).pack(side='top')

myWindow.title('GUI程序练习')  # 窗口大标题
myWindow.geometry('400x250-200-200')  # 窗口位置及位置
myWindow.resizable(0, 0)    # 设置宽高是否可变
myWindow.mainloop()    # 事件循环