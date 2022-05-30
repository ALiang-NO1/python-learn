import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=10, width=20)
b1.pack()
for i in range(1, 11):
    b1.insert('1.0', str(i))
b1.mark_set('mark1', '1.2')
b1.mark_set('mark2', '1.4')
b1.mark_set('mark3', '1.8')


def replace():
    b1.replace('1.2', '1.5', 'replace')


b2 = tk.Button(root, text='Replace', command=replace)
b2.pack()
root.mainloop()

""" replace(index1, index2, chars, args)
将index1与index2之间的字符替换为chars代表的字符。*args可以用来定义标识(tag)。"""