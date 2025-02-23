from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect ball collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    #Detect ball collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    #Detect if right player scores
    if ball.xcor() < -390:
        ball.restart()
        scoreboard.r_player_score()

    #Detect if left player scores
    if ball.xcor() > 390:
        ball.restart()
        scoreboard.l_player_score()









screen.exitonclick()
