from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

LIMIT_FOR_WALL_COLISION = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Day 20 - Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.listen()

game_is_on = True
while game_is_on:
    screen.update() # Updates the screen as tracer was disabled
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() > LIMIT_FOR_WALL_COLISION or snake.head.xcor() < -LIMIT_FOR_WALL_COLISION or snake.head.ycor() > LIMIT_FOR_WALL_COLISION or snake.head.ycor() < -LIMIT_FOR_WALL_COLISION:
        scoreboard.game_over()
        game_is_on = False

    # Detect collision with tail
    for piece in snake.snake_piece[1:]:
        if snake.head.distance(piece) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()