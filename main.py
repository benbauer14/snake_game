from turtle import Screen, Turtle
from snake import Snake
import time


screen = Screen()
screen.setup(600, 600)

screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.update()

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_over = False
while game_over == False:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()