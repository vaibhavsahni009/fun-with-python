#for revision

from turtle import Turtle,Screen
import random 


t=Turtle()
t.width(15)
for i in range(1,8):
    
    t.pencolor(random.choice(['green','blue','red','purple','teal','black']))
    for j in range(i+2):
        t.forward(100)
        t.rt(360/(i+2))


screen=Screen()
screen.exitonclick()