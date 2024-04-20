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
    for car in carman.cars:
        car.move()
        if car.xcor() < -320:
            '''cars moves'''
            car.to_begin()
        if player.distance(car) < 20:
            '''car crash'''
            scoreboard.reset_score()
            for car in carman.cars:
                car.car_speed = 0
            player.next_round()
    if player.ycor() > 280:
        '''player win'''
        scoreboard.update_score()
        for car in carman.cars:
            car.car_speed += 1
        player.next_round()
            

screen.exitonclick()