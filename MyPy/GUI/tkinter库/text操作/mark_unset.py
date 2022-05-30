import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=10, width=20)
b1.pack()
for i in range(1, 11):
    b1.insert('1.0', str(i))

b1.mark_set('mark1', '1.2')
b1.mark_set('mark2', '1.4')
b1.mark_set('mark3', '1.8')
print(b1.mark_names())


def mark_unset():
    b1.mark_unset('mark1', 'mark2')
    print(b1.mark_names())


b2 = tk.Button(root, text='Mark_unset', command=mark_unset)
b2.pack()
root.mainloop()