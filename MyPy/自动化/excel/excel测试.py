from tkinter import Tk, Label, Button, Frame
from openpyxl import Workbook, load_workbook
from random import choice

'a=题目, c=答案, d=选项1, e=, f=, g=选项4'
'a3~g561=单选'
'a563~g769=多选'
'a771~c970判断，a=题目, c=答案'

class HistoryContest(Frame):
    def __init__(self,master, **kw):
        super().__init__(master,**kw)
        self.master=master
        self.pack()
        self.configure(background='beige')
        self.configure(bg='beige')
        self.configure(width=500)
        self.configure(height=400)
        workbook=load_workbook('党史.xlsx')
        self.sheet=workbook['sheet1']
        self.questions=[]
        for i in range(3,562):
            self.questions.append(i)
        self.createWidget()
        self.label_title=Label(self,font='微软雅黑 13',bg='#00aa00',fg='brown')
        self.label_title.pack(padx=5,pady=10,ipadx=5, ipady=5)
        self.label_a=Label(self,font='微软雅黑 12')
        self.label_a.pack(ipadx=5, ipady=5,anchor='w')
        self.label_b=Label(self,font='微软雅黑 12')
        self.label_b.pack(ipadx=5, ipady=5,anchor='w')
        self.label_c=Label(self,font='微软雅黑 12')
        self.label_c.pack(ipadx=5, ipady=5,anchor='w')
        self.label_d=Label(self,font='微软雅黑 12')
        self.label_d.pack(ipadx=5, ipady=5,anchor='w')
        self.answer=Label(self,fg='red')

    def createWidget(self):
        Label(self,text='党史答题系统',font='楷体 18',bg='#bbbb00',fg='red').pack(pady=10)
        # self.show_question()
        button_next=Button(self,text='下一题',command=self.show_question)
        button_next.pack()
        self.answer.pack(side='left')

    def show_question(self):
        data = self.get_question()
        self.label_title.configure(text=data[0].value)
        self.label_a.configure(text='A、'+data[3].value)
        self.label_b.configure(text='B、'+data[4].value)
        self.label_c.configure(text='C、'+data[5].value)
        self.label_d.configure(text='D、'+data[6].value)
        self.answer.configure(text=data[2])

    def get_question(self):
        if self.questions is None:
            print('You have finished all question!')
            self.destroy()
        index=choice(self.questions)
        self.questions.remove(index)
        return self.sheet[f'a{index}:g{index}'][0]

root=Tk()
root.title('答题系统')
root.geometry('500x400-300+200')
app=HistoryContest(master=root)
app.mainloop()