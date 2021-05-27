#for revision

from turtle import Turtle,Screen




t=Turtle()

for _ in range(50):
    t.forward(10)
    t.pu()
    t.forward(10)
    t.pd()



screen=Screen()
screen.exitonclick()