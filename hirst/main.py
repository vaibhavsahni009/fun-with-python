# import colorgram

# colors = colorgram.extract('spot.jpg', 20)

# image_colors=[]

# for i in colors:
#     image_colors.append((i.rgb.r,i.rgb.g,i.rgb.b))

# print(image_colors)
import turtle as turtle_module
import random


colors = [(216, 148, 92), (221, 78, 57), (45, 94, 146), (151, 64, 91), (232, 219, 93), (217, 65, 85), (22, 27, 41), (40, 22, 29),
          (120, 167, 197), (40, 19, 14), (194, 139, 159), (159, 72, 56), (35, 132, 91), (123, 181, 142), (69, 167, 94), (236, 222, 6)]

turtle_module.colormode(255)
t = turtle_module.Turtle()
t.penup()
t.hideturtle()
t.speed('fastest')
t.setheading(235)
t.forward(300)
t.setheading(0)


for i in range(100):
    t.dot(10, random.choice(colors))
    t.forward(30)
    if (i+1) % 10 == 0:
        t.left(90)
        t.forward(30)
        t.left(90)
        t.forward(300)
        t.left(90)
        t.left(90)
screen = turtle_module.Screen()
screen.exitonclick()
