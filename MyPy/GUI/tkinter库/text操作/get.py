import tkinter as tk

root = tk.Tk()
root.geometry('300x200-100+100')

b1 = tk.Text(root, width=26, height=10)
b1.pack()

def get():
    b4['text'] = '结果:'+str(b1.get('1.0', '2.1'))
b2 = tk.Button(root, text='Get', command=get)
b2.pack()

b4 = tk.Label(root, text='结果:')
b4.pack()
root.mainloop()