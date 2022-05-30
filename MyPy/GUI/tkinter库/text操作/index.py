import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=10, width=20)
b1.pack()
b4 = tk.Label(root, text='结果:')


def index():
    b4['text'] = '结果:' + str(b1.index(tk.INSERT))


b2 = tk.Button(root, text='Index', command=index)
b2.pack()
b4.pack()
root.mainloop()