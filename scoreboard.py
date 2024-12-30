from turtle import Turtle
from player import Player
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.goto(-200, 260)
        self.write(f"Level : {self.score}", align="center", font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.score}", align="center", font=FONT)

    def increase(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER !", align="center", font=FONT)



