from turtle import Screen, Turtle
import pandas
from state_class import State
import time
score = 0
us_state = pandas.read_csv("50_states.csv")
us_state_list = us_state['state'].to_list()
us_state_dict = us_state.to_dict()
print(us_state_dict)
# us_state_list = us_state['x'].to_list()
# us_state_list = us_state['y'].to_list()
us = Turtle()
screen = Screen()
screen.title('US State Game')
image = 'blank_states_img.gif'
screen.addshape(image)
us.shape(image)
chosen_states = []
screen.tracer(0)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    state = screen.textinput(title="US states", prompt=f"{score}/50 Choose another state").title()
    if state in us_state_list and state not in chosen_states:
        score += 1
        chosen_states.append(state)
        index = us_state_list.index(state)
        placement = State(state, us_state_dict['x'][index], us_state_dict['y'][index])
    if score == 50:
        print("You won")
        break
    screen.update()



screen.mainloop()
