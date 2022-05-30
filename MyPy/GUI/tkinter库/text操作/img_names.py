import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=15, width=35)
b1.pack()
b4 = tk.Label(root, text='结果:')
p = tk.PhotoImage(file="ab.gif")
p2 = tk.PhotoImage(file="b.gif")

def image():
    b1.image_create('1.0', image=p, name='helloabc')
    b1.image_create('2.0', image=p2, name='image2')


def names():
    b4['text'] = '结果:' + str(b1.image_names())


b2 = tk.Button(root, text='Image', command=image)
b5 = tk.Button(root, text='Imgage_names', command=names)
b2.pack()
b5.pack()
b4.pack()
root.mainloop()