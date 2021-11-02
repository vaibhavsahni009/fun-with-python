STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.goto_starting_postion()
        self.left(90)
    
    def move_car(self):
        self.forward(MOVE_DISTANCE)

    def goto_starting_postion(self):
        # if self.position()[1]>FINISH_LINE_Y:
        self.goto(STARTING_POSITION)
    
    def reached_finished_line(self):
        return self.position()[1]>FINISH_LINE_Y
        