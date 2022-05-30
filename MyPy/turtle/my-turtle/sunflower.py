import turtle as t
import time

t.color('red','yellow')

t.begin_fill()
for _ in range(50):
    t.fd(200)
    t.left(170)
    t.end_fill()

t.mainloop()
