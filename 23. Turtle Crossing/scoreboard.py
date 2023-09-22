from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.goto(-250, 260)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)
    
    def increase_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT, align="center")
