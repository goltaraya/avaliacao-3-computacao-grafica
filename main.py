import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

jimmy = Player()
score = Scoreboard()
car = CarManager()
time_in_sec = 0.1
game_is_on = True

while game_is_on:
    time.sleep(time_in_sec)
    screen.update()
    car.create_car()
    car.move_cars()

    for cars in car.all_cars:
        if jimmy.distance(cars) < 25:
            score.game_over()
            game_is_on = False

    if jimmy.ycor() > 280:
        time_in_sec -= 0.009
        score.level_up()
        car.reset_cars()
        jimmy.goto(0, -280)

    screen.onkeypress(fun=jimmy.move, key="Up")
    screen.listen()

screen.exitonclick()
