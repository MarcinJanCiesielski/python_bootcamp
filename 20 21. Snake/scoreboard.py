from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 20, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align='center', font=('Arial', 20, 'bold'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

