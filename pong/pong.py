import turtle
import os

win=turtle.Screen()
win.title('Pong')
win.bgcolor('black')
win.setup(width=800,height=600)
win.tracer(0)

# Score
score_a = 0
score_b = 0

#paddleA
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddleB
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx=0.04
ball.dy=0.04

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#input funtions
def paddle_a_up():
    y=paddle_a.ycor()
    if y<250:
        y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    if y>-250:
        y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    if y<250:
        y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    if y>-250:
        y-=20
    paddle_b.sety(y)

#taking input
win.listen()
win.onkeypress(paddle_a_up,'w')
win.onkeypress(paddle_a_down,'s')
win.onkeypress(paddle_b_up,'Up')
win.onkeypress(paddle_b_down,'Down')


#mainloop
while True:
    win.update()
    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    # Left and right
    if ball.xcor() > 380:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx *= -1

    elif ball.xcor() < -380:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -330 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.setx(-330)
        ball.dx *= -1
        os.system("aplay bounce.wav&")


    elif ball.xcor() > 330 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.setx(330)
        ball.dx *= -1
        os.system("aplay bounce.wav&")
