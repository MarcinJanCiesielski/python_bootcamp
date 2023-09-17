import turtle as t
import random

FULL_ANGLE = 360

tim = t.Turtle()
tim.speed(0)
screen = t.Screen()
screen.colormode(255)

def rand_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_spirograph(gap_size):
    for _ in range(FULL_ANGLE // gap_size):
        tim.color(rand_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw_spirograph(12)
