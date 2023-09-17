from turtle import Turtle, Screen
import random as rand

tim = Turtle()
tim.shape("turtle")
tim.color("red")

screen = Screen()
screen.colormode(255)

FULL_ANGLE = 360
corners = 3
while corners < 11:
    r, g ,b = rand.randint(0, 256), rand.randint(0, 256), rand.randint(0, 256)
    tim.color(r, g, b)
    for _ in range(0, corners):
        tim.forward(100)
        tim.left(FULL_ANGLE // corners)
    
    corners += 1


screen.exitonclick()
