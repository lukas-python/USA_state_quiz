import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(width=700, height=500)
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
state_list = data.state.to_list()
guessed_state = []
number_of_state_guessed = 0

while len(guessed_state) < 50:
    answer_box = (screen.textinput(title=f"{number_of_state_guessed}/50 States Correct", prompt="What's another state's name")).title()
    if answer_box == 'Exit':
        missing_states = []
        for state in state_list:
            if state not in guessed_state:
                missing_states.append(state)
        states_to_learn = pd.DataFrame(missing_states)
        states_to_learn.to_csv('a.csv')
        break

    if answer_box in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        data_state = data[data.state == answer_box]
        t.goto(int(data_state.x), int(data_state.y))
        t.write(data_state.state.item())
        number_of_state_guessed += 1
        guessed_state.append(answer_box)
