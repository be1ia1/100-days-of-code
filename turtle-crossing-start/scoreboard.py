from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('darkblue')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.goto(0, 250)
        self.write(self.score, align='center', font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()
    
    def reset_score(self):
        self.clear()
        self.score = 0
        self.write_score()

