from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(600, 600)

screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.update()

snake1 = Turtle("square")
snake2= Turtle("square")
snake3 = Turtle("square")

starting_positions = [(0,0), (-10, 0), (-20, 0)]
segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)
    screen.update()

game_over = False
while game_over == False:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(segments) -1 ,0, -1):
        newx = segments[seg - 1].xcor()
        newy = segments[seg - 1].ycor()
        segments[seg].goto(newx, newy)
    segments[0].forward(10)
screen.exitonclick()