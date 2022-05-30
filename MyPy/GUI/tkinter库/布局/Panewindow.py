from tkinter import Tk, PanedWindow, Label

pw = PanedWindow(orient='vertical', bg='brown', showhandle=True, width=200, height=200)
pw.pack(fill='both', expand=True)

top = Label(pw, text='Top pane', bg='pink')
pw.add(top)

bottom = Label(pw, text='Bottom pane', bg='beige')
pw.add(bottom)

pw.mainloop()