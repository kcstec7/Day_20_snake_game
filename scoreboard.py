# Scoreboard class
import turtle
from token import COLON
from turtle import Turtle

ALIGNMENT = "center"
FONT_PROPERTIES = ("Courier", 14, "normal")
COLOR = "light green"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.sety(270)
        self.pencolor(COLOR)
        self.print_score()


    def update_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT_PROPERTIES)

    def game_over(self):
        self.sety(0)
        self.write(f"Game over!", align=ALIGNMENT, font=FONT_PROPERTIES)