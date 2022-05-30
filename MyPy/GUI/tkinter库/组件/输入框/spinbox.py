from tkinter import Tk, Spinbox

root = Tk()
root.title('值输入框')
root.geometry('400x150-100+100')

def print_info():
    print('sp的值：', sp.get())
    if sp.get() == 0:
        sp['state'] = 'disable'

sp = Spinbox(root, from_=0, to=10, command=print_info, activebackground='beige', fg='red',
             increment=2, disabledbackground='red')
sp.pack(pady=10)

sp2 = Spinbox(root, command=print_info, values=('one', {'name': 'AL'}, 22, 280, -22), activebackground='gold')
sp2.pack()

root.mainloop()