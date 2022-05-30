from tkinter import Label, Tk, Button

root = Tk('测试位图')
root.geometry('550x50-100+100')

bitmaps = ['error', 'hourglass', 'info', 'questhead', 'question', 'warning', 'gray12', 'gray25', 'gray50', 'gray75']
for bitmap in bitmaps:
    Label(root, bitmap=bitmap, text=bitmap, compound='top').pack(side='left', padx=3)

Label(root, text='-'*40).pack()

reliefs = ['flat', 'groove', 'raised', 'ridge', 'solid', 'sunken']
for relief in reliefs:
    Button(root, relief=relief, text=relief).pack(side='left', padx=3)

root.mainloop()