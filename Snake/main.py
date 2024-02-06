import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
score = Scoreboard()
snake = Snake()
food = Food()
border = 280

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #Detect colision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()


    #Detect colision with wall
    if snake.head.xcor() > border or snake.head.xcor() < -border or snake.head.ycor() > border or snake.head.ycor() < -border:
        score.reset()
        snake.reset()


    #Detect colision with tail
    for segments in snake.snake_seg[1:]:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            score.reset()
            snake.reset()














screen.exitonclick()