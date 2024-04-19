from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):
    
    def __init__(self, position) -> None:
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setx(position[0])
        self.sety(position[1])

    def up(self):
        new_y = self.ycor()
        if new_y <= 225:
            new_y += MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
    
    def down(self):
        new_y = self.ycor()
        if new_y >= -220:
            new_y -= MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def stop(self):
        pass