import turtle as t
import random

colors = [(62, 100, 108), (251, 245, 244), (196, 76, 67), (212, 153, 67), (157, 167, 162), (83, 184, 168), (231, 199, 146), (216, 143, 140), (220, 197, 195)]

FULL_ANGLE = 360

tim = t.Turtle()
tim.speed(0)
screen = t.Screen()
screen.colormode(255)
tim.hideturtle()
tim.penup()

tim.setheading(223)
tim.forward(620)
tim.setheading(0)

for _ in range(19):
    for i in range(19):
        tim.dot(20, random.choice(colors))
        tim.forward(50)

    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(19*50)
    tim.setheading(0)

screen.exitonclick()
