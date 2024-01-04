from turtle import Screen

from paddle import Paddle
from pong_ball import Ball
from scoreboard import Scoreboard
import time

game_status = 0

screen = Screen()
screen.setup(height=600, width=1000)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer()

scoreboard = Scoreboard()
paddle1 = Paddle((470, 0))
paddle2 = Paddle((-470, 0))
pong_ball = Ball()


screen.onkey(lambda: paddle1.up(), "Up")
screen.onkey(lambda: paddle1.down(), "Down")


def computer_paddle_move():
    """Decide which logic u want to implement"""

    # play as player
    # if int(paddle2.heading()) == 90 and int(paddle2.ycor()) < 260:
    #     paddle2.up()
    # elif int(paddle2.heading()) == 270 and int(paddle2.ycor()) > -240:
    #     paddle2.down()
    # else:
    #     paddle2.setheading(360-paddle2.heading())
    #     paddle2.forward(paddle.MOVE_DISTANCE)

    # play vs ideal computer
    paddle2.goto(paddle2.xcor(), pong_ball.ycor())


def collision_with_wall():
    if pong_ball.ycor() > 260 or pong_ball.ycor() < -260:
        pong_ball.bounce_horizontally()


def collision_with_pad():
    if pong_ball.distance(paddle1) < 40 and pong_ball.xcor() > 440 or pong_ball.distance(paddle2) < 40 and \
            pong_ball.xcor() < -440:
        pong_ball.bounce_vertically()


def pong_ball_misses_paddle():
    if pong_ball.xcor() > 500:
        scoreboard.add_score_2()
        return True
    elif pong_ball.xcor() < -500:
        scoreboard.add_score_1()
        return True
    else:
        return False


screen.listen()

while game_status < 5:
    time.sleep(0.01)
    screen.update()
    pong_ball.move()
    collision_with_wall()
    collision_with_pad()
    computer_paddle_move()
    if pong_ball_misses_paddle():
        pong_ball.go_home()
        game_status += 1

scoreboard.game_over()

screen.exitonclick()
