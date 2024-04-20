from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager():
    def __init__(self):
        self.cars = []
        for car_number in range(0, 40):
            car = Car(random.choice(COLORS))
            self.cars.append(car)


class Car(Turtle):

    def __init__(self, color):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(color)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.car_speed = 0
        self.setheading(180)
        self.goto(random.randint(150, 900), random.randint(-260, 260))

    def move(self):
        car_speed = STARTING_MOVE_DISTANCE + self.car_speed
        self.forward(car_speed)

    def to_begin(self):
        self.hideturtle()
        self.goto(320, random.randint(-260, 260))
        self.showturtle()