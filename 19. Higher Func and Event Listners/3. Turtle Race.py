from random import randint
from turtle import Screen, Turtle

is_race_on = False
winner = ''

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win th race? Enter a color:")

if user_bet:
    is_race_on = True

turtles = []
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def create_turtles():
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        turtles.append(new_turtle)

def position_turtles():
    y_position = -120
    x_position = -230
    space_between = 50
    # for i in range(len(turtles)):
    #     turtles[i].goto(x=x_position, y=y_position + i * space_between)
    for i, turtle in enumerate(turtles):
        turtle.goto(x=x_position, y=y_position + i * space_between)

def move_turtles():
    for turtle in turtles:
        move = randint(0, 10)
        turtle.forward(move)

def is_winner():
    global is_race_on
    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            return turtle.pencolor()
    return ''

create_turtles()
position_turtles()

while is_race_on:
    move_turtles()
    winner_color = is_winner()

if winner_color == user_bet:
    print(f"You've won! The {winner_color} turtle is the winner!")
else:
    print(f"You've lost! The {winner_color} turtle is the winner!")

screen.exitonclick()
