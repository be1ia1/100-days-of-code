from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open('high_score.txt') as fo:
            self.high_score = int(fo.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}",
                    align='center', font=('Arial', 24, 'normal'))

    def increase(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', 'w') as fo:
                fo.write(str(self.high_score))
        self.score = 0
        self.update()
