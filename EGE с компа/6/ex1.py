from turtle import *

tracer(0)
lt(90)
screensize(3000, 3000)
m = 20

for _ in range(2):
    fd(14 * m)
    lt(270)
    bk(12 * m)
    rt(90)

up()

fd(9 * m)
rt(90)
bk(7 * m)
lt(90)

down()

for _ in range(2):
    fd(13 * m)
    rt(90)
    fd(6 * m)
    rt(90)

up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * m, y * m)
        dot(3, 'red')

update()
done()
