from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="turtle")
        self.penup()
        self.setheading(90)
        self.speed("fastest")
        self.go_to_start_position()

    def move(self):
        new_x = self.xcor()
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x, new_y)

    def go_to_start_position(self):
        self.goto(STARTING_POSITION)

    def is_player_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y
