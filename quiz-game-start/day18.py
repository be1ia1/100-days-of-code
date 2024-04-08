from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)


timmy = Turtle()
timmy.shape("turtle")
# timmy.color("darkblue")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# for _ in range(0,100,10):
# timmy.teleport(x=-400)
# print(timmy.position())
# timmy.pensize(2)
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


sides = 3
while sides <= 9:
    cur_angle = 360 / sides
    for _ in range(sides):
        timmy.forward(50)
        timmy.right(cur_angle)
        timmy.forward(50)
    sides += 1
    timmy.pencolor(randint(0,255), randint(0,255), randint(0,255))



screen.exitonclick()