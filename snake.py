# Snake class
import time
from turtle import Turtle

MOVE_DISTANCE = 20
DEGREES_UP    = 90
DEGREES_DOWN  = 270
DEGREES_LEFT  = 180
DEGREES_RIGHT = 0

class Snake:

    snake_piece = []
    position_x = 0

    # add a constructor to the class
    def __init__(self):
        self.snake_piece = []
        self.create_snake()
        self.head = self.snake_piece[0]

    def create_snake(self):
        for i in range(3):
            self.extend()

    def move(self):

        snake_positions = len(self.snake_piece) - 1

        # start= snake_positions, stop= 0, step= -1
        for piece_position in range(snake_positions, 0, -1):
            position_x = self.snake_piece[piece_position - 1].xcor()
            position_y = self.snake_piece[piece_position - 1].ycor()
            self.snake_piece[piece_position].goto(position_x, position_y)

        self.head.forward(MOVE_DISTANCE)

    # Representation of degrees from the ORIGINAL heading of the snake:
    # 0º = RIGHT, 90º = UP, 180º = LEFT, 270º = DOWN
    # snake_piece[0] is the "head" of the snake, which will make its entire body move
    # In the official game, the snake cannot move directly from its immediate opposite heading

    def up(self):
        if self.head.heading() != DEGREES_DOWN:
            self.head.setheading(DEGREES_UP)

    def down(self):
        if self.head.heading() != DEGREES_UP:
            self.head.setheading(DEGREES_DOWN)

    def left(self):
        if self.head.heading() != DEGREES_RIGHT:
            self.head.setheading(DEGREES_LEFT)

    def right(self):
        if self.head.heading() != DEGREES_LEFT:
            self.head.setheading(DEGREES_RIGHT)

    def add_piece(self, position):
        square_turtle = Turtle(shape="square")
        square_turtle.color("white")
        square_turtle.penup()
        square_turtle.goto(position)
        self.snake_piece.append(square_turtle)

    def extend(self):
        if len(self.snake_piece) > 0:
            self.add_piece(self.snake_piece[-1].position())
        else:
            self.add_piece((0, 0))