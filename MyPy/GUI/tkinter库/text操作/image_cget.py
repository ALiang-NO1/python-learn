import tkinter as tk

root = tk.Tk()
root.geometry('300x200-100+100')

def image():
    p = tk.PhotoImage(file="pornhub.png")
    b1.image_create(tk.END, image=p, name='createdImage')

def config():
    b1.image_configure('1.0', name='cccc')
    b4['text'] = '结果:' + str(b1.image_cget('1.0', 'name'))

b1 = tk.Text(root, width=26, height=10)
b1.pack()

b2 = tk.Button(root, text='Image', command=image)
b2.pack(side='left')

b5 = tk.Button(root, text='Imgage_configure', command=config)
b5.pack(side='left')

b4 = tk.Label(root, text='结果:')
b4.pack(side='left')
root.mainloop()