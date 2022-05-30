import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("消息框测试")
root.geometry('380x60-100+100')

def m1(e):
    info = tk.messagebox.showinfo('消息', '我爱你', icon='warning')
    print('showinfo:', info)  # 返回 string 类型
def m2(e):
    warning = tk.messagebox.showwarning('警告', '你将删除所有文件！')
    print('showwarning:', warning)
def m3(e):
    error = tk.messagebox.showerror('错误提示', '输入错误')
    print('showerror:', error)
def m4(e):
    question = tk.messagebox.askquestion('问题', '你有人爱吗？')
    print('askquestion:', question)
def m5(e):
    okcancel = tk.messagebox.askokcancel('是否取消', '是否取消选择？')
    print('okcancel:', okcancel)
def m6(e):
    yesno = tk.messagebox.askyesno('是否', 'Y-N')
    print('yesno:', yesno)
def m7(e):
    yesnocancel = tk.messagebox.askyesnocancel('是否取消', 'Y-N-C')
    print('yesnocancel:', yesnocancel)

b1 = tk.Button(root, text="消息", padx=2)
b1.bind('<1>', m1); b1.pack(side='left')

b2 = tk.Button(root, text="警告", padx=2)
b2.bind('<1>', m2); b2.pack(side='left')

b3 = tk.Button(root, text="错误提示", padx=2)
b3.bind('<1>', m3); b3.pack(side='left')

b4 = tk.Button(root, text="问题", padx=2)
b4.bind('<1>', m4); b4.pack(side='left')

b5 = tk.Button(root, text="是否取消", padx=2)
b5.bind('<1>', m5); b5.pack(side='left')

b6 = tk.Button(root, text="是否", padx=2)
b6.bind('<1>', m6); b6.pack(side='left')

b7 = tk.Button(root, text="是否取消")
b7.bind('<1>', m7); b7.pack(side='left')

root.mainloop()