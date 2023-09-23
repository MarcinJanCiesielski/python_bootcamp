from turtle import Turtle

FILE_NAME = "high_score.txt"

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        self.score = 0
        self.high_core = self.read_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_core}", move=False, align='center', font=('Arial', 20, 'bold'))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align='center', font=('Arial', 20, 'bold'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_core:
            self.high_core = self.score
            self.write_high_score(self.high_core)
        self.score = 0
        self.update_scoreboard()

    def read_high_score(self):
        with open(FILE_NAME, encoding="utf8") as file:
            return int(file.read())

    def write_high_score(self, highscore):
        with open(FILE_NAME, encoding="utf8", mode="w") as file:
            file.write(highscore)
