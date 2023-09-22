from turtle import Turtle
ALIGNMENT = "center"
FONT = ('algerian', 15, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.show_score()

    def show_score(self):
        self.write(f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER !!", move=False, align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.clear()
        self.show_score()
