import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    if snake.snakes[0].xcor() > 280 or snake.snakes[0].xcor() < -280 or snake.snakes[0].ycor() > 280 or -280 > \
            snake.snakes[0].ycor():
        is_game_on = False
        scoreboard.game_oever()

    for segment in snake.snakes[1:]:
        if snake.snakes[0].distance(segment) < 10:
            is_game_on = False
            scoreboard.game_oever()

screen.exitonclick()
