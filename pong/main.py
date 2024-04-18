import turtle
from paddle import Paddle

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

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

screen.exitonclick()