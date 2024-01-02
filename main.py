from turtle import Screen

import paddle
from paddle import Paddle
from pong_ball import Ball
import time


game_status = True

screen = Screen()
screen.setup(height=600, width=1000)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer()


paddle1 = Paddle((470, 0))
paddle2 = Paddle((-470, 0))
pong_ball = Ball()


screen.onkey(lambda: paddle1.up(), "Up")
screen.onkey(lambda: paddle1.down(), "Down")


def computer_paddle_move():
    if int(paddle2.heading()) == 90 and int(paddle2.ycor()) < 260:
        paddle2.up()
    elif int(paddle2.heading()) == 270 and int(paddle2.ycor()) > -260:
        paddle2.down()
    else:
        paddle2.setheading(360-paddle2.heading())
        paddle2.forward(paddle.MOVE_DISTANCE)

screen.listen()

while game_status:
    screen.update()
    time.sleep(0.05)
    pong_ball.move()
    computer_paddle_move()



screen.exitonclick()