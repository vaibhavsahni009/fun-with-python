COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle, width
import random
class CarManager:

    def __init__(self) :
        super().__init__()
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
        
        
    def create_car(self):
        if random.randint(1,6)==1:
            new_car =Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.pu()
            new_car.goto((300,random.randint(-250,250)))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
            
    def increment_level(self):
        self.car_speed+=MOVE_INCREMENT

