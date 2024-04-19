from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.step_x = 10
        self.step_y = 10
        self.move_speed = 0.1
    
    def move(self):
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)

    def return_ball(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()

    def bounce_y(self):
        self.step_y *= -1

    
    def bounce_x(self):
        self.step_x *= -1
        self.move_speed *= 0.9