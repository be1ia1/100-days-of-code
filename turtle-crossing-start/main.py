import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
carman = CarManager()

screen.listen()

screen.onkey(screen.bye, 'Escape')
screen.onkey(player.move_up, 'Up')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carman.create_car()
    carman.move()
    # print(len(carman.cars))

    for car in carman.cars:
        if player.distance(car) < 20:
            '''car crash'''
            scoreboard.reset_score()
            carman.car_speed = 0
            player.next_round()
        if player.ycor() > 280:
            '''player win round'''
            scoreboard.update_score()
            carman.level_up()
            player.next_round()
        if car.xcor() < -310:
            carman.cars.remove(car)


screen.exitonclick()
