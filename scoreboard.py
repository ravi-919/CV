from turtle import Turtle

X_COR = 0
Y_COR = 280
ALIGNMENT = 'CENTER'
FONT = ('Comic Sans MS', 12, 'italic')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.points = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.goto((X_COR, Y_COR))
        self.speed('fastest')
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f'Score = {self.points},   HighScore = {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode="w") as file:
                file.write(f"{self.points}")
        self.points = 0
        self.print_score()

    def score_update(self):
        self.points += 1
        self.print_score()