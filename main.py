from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle(350)
paddle2 = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=paddle1.up, key="Up")
screen.onkey(fun=paddle1.down, key="Down")

screen.onkey(fun=paddle2.up, key="q")
screen.onkey(fun=paddle2.down, key="a")

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall:
    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    #Detect collision with right paddle:
    if ball.distance(paddle1) < 50 and abs(ball.xcor()) > 320:
        ball.bounce_x()


    if ball.distance(paddle2) < 50 and abs(ball.xcor()) > 320:
        ball.bounce_x()


    #Detect right paddle miss:
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    #Detect left paddle mis
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()
