import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
screen.listen()
screen.onkeypress(player.move_car,"Up")
carManager=CarManager()
scoreBoard=Scoreboard()
i=0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # if i==6:
    #     i=0
    carManager.create_car()
    carManager.move()

    if player.reached_finished_line():
        player.goto_starting_postion()
        carManager.increment_level()
        scoreBoard.increment_level()

    for car in carManager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreBoard.game_over()

    screen.update()


screen.exitonclick()