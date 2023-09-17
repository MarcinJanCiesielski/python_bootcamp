import turtle as t
import random

tim = t.Turtle()
tim.pensize(15)
tim.speed(0)
screen = t.Screen()
screen.colormode(255)

def rand_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def make_move(length):
    angles = [0, 90, 180, 270]

    tim.color( rand_color() )
    tim.setheading(random.choice(angles))

    tim.forward(length)

for _ in range(200):
    make_move(30)


screen.exitonclick()
