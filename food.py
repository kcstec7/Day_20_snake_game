# Food class
from turtle import Turtle
import random

# Adding "Turtle" class to "Food" class by inheritance
class Food(Turtle):
    def __init__(self):
        super().__init__()   # This makes the constructor of "Turtle" class to be called
        self.shape("star") # "shape" is a method of "Turtle" class
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # The default size is 20x20. So, we are reducing to the half of that
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # We're using 280 as we don't want the food to go to the limits of the screen
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)