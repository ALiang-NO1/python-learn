from tkinter import Tk, Button
from tkinter.ttk import Separator
root = Tk()
root.geometry('400x150-100+100')

cursors = ['arrow', 'based_arrow_down', 'boat', 'bogosity', 'bottom_left_corner']
for cursor in cursors:
    Button(root, text=cursor, cursor=cursor, relief='ridge').pack(side='left', padx=2, anchor='n')  # width=4, height=1,

Separator(root, orient='horizontal').pack(fill='x', pady=5)

root.mainloop()
