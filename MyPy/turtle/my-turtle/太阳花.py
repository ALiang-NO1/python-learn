from turtle import *

color('red', 'yellow')
begin_fill()
while True:
    fd(200)
    lt(170)
    if abs(pos()) < 1:
        break
end_fill()
done()