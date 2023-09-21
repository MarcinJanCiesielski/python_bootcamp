from turtle import Turtle

MOVE_FACTOR = 20

class Paddle(Turtle):
    def __init__(self, position) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_x = self.xcor()
        new_y = self.ycor() + MOVE_FACTOR
        self.goto(new_x, new_y)

    def go_down(self):
        new_x = self.xcor()
        new_y = self.ycor() - MOVE_FACTOR
        self.goto(new_x, new_y)
