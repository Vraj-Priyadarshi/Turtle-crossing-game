from turtle import Turtle, Screen
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.carspeed = STARTING_MOVE_DISTANCE


    def create_car(self):
        new_chance = random.randint(1,5)
        if new_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):

        for car in self.all_cars:
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT
















