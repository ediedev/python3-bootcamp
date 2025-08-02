import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(600, 400)
screen.title("Map U.S. State Game")
image = "blank-states-img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

data = pd.read_csv("50_states.csv")
states_data = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct",
                                    prompt="What is another states's name?").title()
    if answer_state == "Exit":
        # missed_states = []
        # for state in states_data:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        #
    #Modified with list comprehension
        missed_states = [state for state in states_data
                         if state not in guessed_states]

        pd.DataFrame(missed_states).to_csv("states_to_learn.csv")
    if answer_state in states_data:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)