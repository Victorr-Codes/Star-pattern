import turtle
t = turtle.Turtle()
t.speed(0)
angle = 0
size = 5
while 1:
    for i in range(5):
        t.forward(250)
        t.right(144)
    t.right(size)
    angle += 1
    if angle >= 360 / size:
        break
turtle.done()
