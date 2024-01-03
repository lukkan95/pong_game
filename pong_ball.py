from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("blue")
        self.speed(0)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_horizontally(self):
        if self.y_move == 10:
            self.y_move = -10
        else:
            self.y_move = 10

    def bounce_vertically(self):
        if self.x_move == 10:
            self.x_move = -10
        else:
            self.x_move = 10

    def go_home(self):
        self.x_move = 10
        self.y_move = 10
        self.goto(self.x_move, self.y_move)


