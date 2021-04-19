import turtle as t
import time as ti
from itertools import cycle

colors = cycle(['red','orange','yellow','blue','green','purple','white','violet','indigo','silver'])

def draw_circle(size,angle,shift):
    t.color(next(colors))
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.right(angle)
    t.forward(shift)
    t.color(next(colors))
    t.begin_fill()
    for i in range(4):
        t.forward(2*size)
        t.left(90)
    t.end_fill()
    draw_circle(size + 10,angle+5,shift+1)

t.bgcolor('black')
t.speed('fast')
t.pensize(2)

draw_circle(30,0,1)

ti.sleep(3)
t.hideturtle()
