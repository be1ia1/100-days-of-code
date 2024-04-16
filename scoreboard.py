from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)

    def update(self):
        self.clear()
        self.score += 1

    def write_score(self):
        self.write(f"Score: {self.score}", align='center', font=('Arial', 24, 'normal'))

