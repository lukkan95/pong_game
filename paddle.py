from turtle import Turtle
import random

# STARTING_POSITIONS = (480, 0)
MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(position)

    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)




    # def heading(self):
    #     super().heading()


