from tkinter import PanedWindow, Entry, Scale, LabelFrame

pw = PanedWindow(orient='horizontal', bg='brown', showhandle=True, width=400, height=400)
pw.pack(fill='both', expand=True, padx=10, pady=10)

entry = Entry(pw, bd=3)
pw.add(entry)

pwin = PanedWindow(pw, orient='vertical')
pw.add(pwin)

scale = Scale(pwin, orient='vertical')
pwin.add(scale)

left_frame = LabelFrame(pw, text='left pane', width=120, height=150)
pw.add(left_frame)

left_frame = LabelFrame(pw, text='middle pane', width=120)
pw.add(left_frame)

left_frame = LabelFrame(pw, text='right pane', width=120)
pw.add(left_frame)

pw.mainloop()