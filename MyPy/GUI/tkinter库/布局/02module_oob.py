from tkinter import *
from tkinter import messagebox

class Application(Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        pass

if __name__ == '__main__':
    root = Tk()
    root.geometry('200x120-100+100')
    app = Application(master=root)
    root.mainloop()