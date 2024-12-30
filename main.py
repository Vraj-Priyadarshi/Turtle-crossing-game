import time
from turtle import Screen
from player import Player
import random
from carmanager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
screen.update()

carmanager = CarManager()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_car()

    if player.ycor() > 280:
        player.goto(0, -280)
        carmanager.level_up()
        scoreboard.increase()



    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()





