from tkinter import Tk, Label

root = Tk()
root.title('pack方法测试')
root.geometry('-100+100')

print('执行前：', root.pack_slaves())

l2 = Label(root, text='标签1', font='Times 20 bold', width=6, bg='gold')
l2.pack(side='left', padx=12, pady=10, anchor='s')
l3 = Label(root, text='标签2', font='Times 20 bold', bg='gold')
l3.pack(side='left', padx=10, pady=10, anchor='s')

print('执行后：', root.pack_slaves())
print('info：', Label.pack_info(l2))
print('info：', Label.pack_info(l3))
print('size：', l2.size())
l3.pack_forget()

root.mainloop()