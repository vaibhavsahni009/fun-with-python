from turtle import Turtle,Screen

t=Turtle()
screen=Screen()

def move_forwards():
    t.forward(10)
def move_backwards():
    t.backward(10)
def turn_right():
    t.right(10)
def turn_left():
    t.left(10)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.listen()
screen.onkey(key='Up',fun=move_forwards)
screen.onkey(key='Down',fun=move_backwards)
screen.onkey(key='Left',fun=turn_left)
screen.onkey(key='Right',fun=turn_right)
screen.onkey(key='space',fun=clear)

screen.exitonclick()