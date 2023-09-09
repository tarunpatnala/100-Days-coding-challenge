from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from score_board import Scoreboard


screen = Screen()
screen.title("Turtle - The crossing capstone")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        scoreboard.increase_level()


screen.exitonclick()
