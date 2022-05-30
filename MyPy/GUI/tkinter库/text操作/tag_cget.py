import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=10, width=20)
b1.pack()


def tag():
    b1.tag_add('second', '2.1', '2.2')
    b1.tag_configure('second', relief=tk.GROOVE)
    print(b1.tag_cget('second', 'relief'))


b2 = tk.Button(root, text='Tag', command=tag)
b2.pack()

root.mainloop()