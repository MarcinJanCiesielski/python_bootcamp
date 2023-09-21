from turtle import Turtle

MOVE_FACTOR = 10

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = MOVE_FACTOR
        self.y_move = MOVE_FACTOR
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    
    def bounce_y(self):
        self.y_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
