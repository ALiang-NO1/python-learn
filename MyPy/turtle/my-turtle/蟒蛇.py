from turtle import *

setup(650, 350, -200, 200)
pu()
fd(-250)
pd()
pensize(25)
pencolor('purple')
seth(-40)
for i in range(4):
    circle(40, 80)
    circle(-40, 80)
circle(40, 80/2)
fd(40)
circle(16, 80)
fd(40 * 2/3)
mainloop()