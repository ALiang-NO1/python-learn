from turtle import *
import time

pensize(5)
color('yellow','red')

begin_fill()
for _ in range(5):
    fd(200)
    right(144)
end_fill()
time.sleep(2)

pu()
goto(-150,-120)
color('violet')
write('Done',font = ('Arial',40,'normal'))

mainloop()
