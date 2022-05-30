from tkinter import Tk, Label

root = Tk()
root.title('测试After函数')

num = 0
def run(digit):
    def count():
        global num
        num += 1
        print(num)
        digit.config(text=str(num))
        digit.after(1000, count)
    count()
digit = Label(root, text=0, fg='red', bg='gold', font='Helvetic 20 bold')
digit.pack()
run(digit)

root.mainloop()