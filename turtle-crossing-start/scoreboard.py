from time import sleep
from turtle import Turtle


FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.pu()
        self.goto(-280,250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left",font=FONT)

    def increment_level(self):
        self.level+=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=FONT)


