import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, )
b1.pack()
p = tk.PhotoImage(file="a.gif")


def image():
    b1.image_create(tk.END, image=p)


b2 = tk.Button(root, text='Image', command=image)
b2.pack()
root.mainloop()