from turtle import Turtle
import random

STARTING_POSITION = [random.randint(-30, 30), random.randint(-210, -150)]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("blue")
        self.speed(30)
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.penup()
        self.starting_move()

    def starting_move(self):
        print(STARTING_POSITION)
        self.setheading(random.choice(STARTING_POSITION))

    def move(self):
        self.forward(30)

