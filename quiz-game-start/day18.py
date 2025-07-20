from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
screen.colormode(255)


timmy = Turtle()
timmy.shape("turtle")
timmy.color("darkblue")

# for _ in range(10):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)


# sides = 3
# for _ in range(10):
#     angle = 360 / sides
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#     sides +=1
#     new_color = (randint(0, 256), randint(0, 256), randint(0, 256))
#     timmy.pencolor(new_color)


# timmy.pensize(10)
timmy.speed(1000)
# angles = [0, 90, 180, 270]
# for _ in range(200):
#     timmy.pendown()
#     new_color = (randint(0, 255), randint(0, 255), randint(0, 255))
#     timmy.pencolor(new_color)
#     timmy.forward(30)
#     timmy.setheading(choice(angles))
    

radius = 100
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        new_color = (randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.pencolor(new_color)
        timmy.circle(radius)

        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(15)










# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# for _ in range(0,100,10):
#     timmy.teleport(x=-400)
#     print(timmy.position())
#     timmy.pensize(2)
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# sides = 3
# while sides <= 9:
#     cur_angle = 360 / sides
#     for _ in range(sides):
#         timmy.forward(50)
#         timmy.right(cur_angle)
#         timmy.forward(50)
#     sides += 1
#     timmy.pencolor(randint(0,255), randint(0,255), randint(0,255))



screen.exitonclick()