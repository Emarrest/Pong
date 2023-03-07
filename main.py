from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.listen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.colormode(255)
screen.bgcolor("black")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.moveup, "Up")
screen.onkey(r_paddle.movedown, "Down")
screen.onkey(l_paddle.moveup, "w")
screen.onkey(l_paddle.movedown, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.off_limits()
        scoreboard.l_point()
        ball.bounce_x()
    elif ball.xcor() < -400:
        ball.off_limits()
        scoreboard.r_point()
        ball.bounce_x()

screen.exitonclick()