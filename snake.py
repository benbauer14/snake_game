from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-10, 0), (-20, 0)]

class Snake:
    def __init__(self):
        self.segments = []

def createSnake():

    for position in STARTING_POSITIONS:
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
