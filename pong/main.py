import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

scoreboard = Scoreboard()

ball = Ball()

screen.listen()
screen.onkeypress(right_paddle.up, 'Up')
screen.onkeypress(right_paddle.down, 'Down')
screen.onkeypress(left_paddle.up, 'w')
screen.onkeypress(left_paddle.down, 's')

screen.onkeyrelease(right_paddle.stop, 'Up')
screen.onkeyrelease(right_paddle.stop, 'Down')
screen.onkeyrelease(left_paddle.stop, 'Up')
screen.onkeyrelease(left_paddle.stop, 'Up')

is_on = True
while is_on:
    screen.update()
    time.sleep(ball.move_speed)

    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()    

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
        (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.return_ball()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.return_ball()
        scoreboard.r_point()

screen.exitonclick()