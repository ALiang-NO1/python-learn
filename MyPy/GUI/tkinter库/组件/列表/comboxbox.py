from tkinter import Tk, StringVar, Label
from tkinter.ttk import Combobox

root = Tk()
root.title('测试Combobox')
root.geometry('400x150-100+100')

def combo_select(event):
    label_var.set(var.get())

var = StringVar()
cb = Combobox(root, textvariable=var)
cb['value'] = ('py', 'ruby', 'js', 'c++')
cb.current(0)  # 或者 cb.set('py')
cb.bind('<<ComboboxSelected>>', combo_select)
cb.pack(pady=10)

label_var = StringVar()
label = Label(root, textvariable=label_var, bg='pink', relief='ridge')
label_var.set(var.get())
label.pack()

root.mainloop()