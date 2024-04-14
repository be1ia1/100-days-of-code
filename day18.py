import turtle
from random import randint

screen = turtle.Screen()
screen.colormode(255)


timmy = turtle.Turtle()

timmy.speed("fastest")
timmy.pensize(5)

def draw_spirograph(size_of_gap):
    """Draw spirograph with defined size of gap."""
    for _ in range(int(360 / size_of_gap)):
        timmy.color(randint(0,255), randint(0,255), randint(0,255))
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


draw_spirograph(15)

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