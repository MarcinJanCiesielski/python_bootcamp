import turtle
import pandas

states_data = pandas.read_csv("./50_states.csv")
all_states = states_data.state.to_list()
IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. Stares Game")
screen.bgpic(IMAGE)

def create_state_writer():
    state_turtle = turtle.Turtle()
    state_turtle.penup()
    state_turtle.color("black")
    state_turtle.speed("fastest")
    state_turtle.hideturtle()
    return state_turtle

states_name_writer = create_state_writer()
guessed_states = []

game_is_on = True

while game_is_on:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    state = states_data[states_data.state == answer_state]
    if not state.empty:
        guessed_states.append(answer_state)
        x = int(state.x.item())
        y = int(state.y.item())
        states_name_writer.goto(x,y)
        states_name_writer.write(state.state.item())
    else:
        game_is_on = False

missed_states = [state for state in all_states if state not in guessed_states]

new_data = pandas.DataFrame(missed_states)
new_data.to_csv("state_to_learn.csv")
