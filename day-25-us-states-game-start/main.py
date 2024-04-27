import turtle
import pandas as pd

data = pd.read_csv('50_states.csv')
# states = data.state


screen = turtle.Screen()
screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

timmy = turtle.Turtle()
timmy.penup()
timmy.hideturtle()

is_on = True
correct = []

while is_on:
    answer_state = screen.textinput(title="Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state in data.state.values:
        correct.append(answer_state)
        state_data = data[data.state == answer_state]
        timmy.goto(int(state_data.x), int(state_data.y))
        timmy.write(answer_state, align='center')    
    print(len(correct))

screen.mainloop()
