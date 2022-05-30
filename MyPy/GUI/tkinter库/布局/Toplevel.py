from tkinter import Tk, Toplevel, Label

root = Tk()
root.title('Toplevel测试主窗口')
root.geometry('400x150-100+100')

tl = Toplevel()
tl.title = 'Toplevel窗口'
tl.geometry('300x180')
Label(tl, text='I am a Toplevel').pack()

root.mainloop()
