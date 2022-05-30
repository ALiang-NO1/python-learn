from tkinter import Tk, Entry, Button, Checkbutton, BooleanVar

root = Tk()
root.title('操作输入框')
root.geometry('240x80-100+100')

entry = Entry(root, relief='sunken', bg='lightblue')
entry.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky='w')

Button(root, text='选取', command=lambda: entry.select_range(0, 'end'))\
    .grid(row=1, column=0, padx=5, pady=5, sticky='w')

Button(root, text='取消选取', command=lambda: entry.select_clear())\
    .grid(row=1, column=1, padx=5, pady=5, sticky='w')

Button(root, text='删除', command=lambda: entry.delete(0, 'end'))\
    .grid(row=1, column=2, padx=5, pady=5, sticky='w')

Button(root, text='结束', command=lambda: root.destroy())\
    .grid(row=1, column=3, padx=5, pady=5, sticky='w')

def readonly():
    if var.get():
        entry['state'] = 'disable'
    else:
        entry['state'] = 'normal'

var = BooleanVar()
Checkbutton(root, text='只读', command=readonly, variable=var).grid(row=0, column=3)

root.mainloop()