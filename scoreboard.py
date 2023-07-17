from turtle import Turtle
FONT = ("arial", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(r"highscore") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(-200, 360)
        self.color("white")
        self.update_scoreboard()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"highscore", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"The Score : {self.score}   |   High Score : {self.high_score}", font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


