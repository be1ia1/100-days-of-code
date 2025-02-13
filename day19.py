import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []


user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')



y_pos = -90

for color in colors:
    timmy = turtle.Turtle(shape='turtle')
    timmy.penup()
    timmy.color(color)
    timmy.goto(-235, y_pos)
    y_pos += 30
    turtles.append(timmy)

# if user_bet:
#     is_race_on = True

winner = None
is_race_on = True

while is_race_on:
    for tle in turtles:
        step = random.randint(0,10)
        tle.forward(step)
        if tle.xcor() >= 235:
            winner = tle.color()[0]
            is_race_on = False

if winner == user_bet:
    print(f"You win! With {user_bet}..")
else:
    print(f"You lose.. Winner is {winner}")




screen.exitonclick()