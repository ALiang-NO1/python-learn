from tkinter import Tk, Button, messagebox

root = Tk()
root.title('按钮绑定多事件')
root.geometry('400x150-100+100')

def func():
    ret = messagebox.askokcancel('OKCANCEL', '结束或取消？')
    if ret:
        root.destroy()
    else:
        return

def func2(e):
    print('按下了：', e.char + '键')

btn = Button(root, text='click me', command=func)
btn.pack(anchor='w', padx=10, pady=10)
btn.bind('<Key>', func2, add='+')

root.mainloop()
