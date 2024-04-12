import turtle
from random import randint

screen = turtle.Screen()
screen.colormode(255)


timmy = turtle.Turtle()

timmy.speed("fastest")
timmy.pensize(5)

for _ in range(0, 50):
    timmy.color(randint(0,255), randint(0,255), randint(0,255))
    timmy.circle(80)
    cur_heading = timmy.heading()
    timmy.setheading(cur_heading + 10)


# distance = 20
# angles = [0, 90, 180, 270]


# directions = ['f', 'b']


# timmy.pensize(5)

# max_steps = 200
# while max_steps >= 0:
#     timmy.color(choice(colours))
#     # cur_direction = choice(directions)
#     timmy.forward(distance) # if cur_direction == 'f' else timmy.backward(distance)
#     cur_angle = choice(angles)
#     # timmy.right(cur_angle) if cur_direction == 'f' else timmy.left(cur_angle)
#     timmy.setheading(cur_angle)

#     max_steps -= 1


screen.exitonclick()