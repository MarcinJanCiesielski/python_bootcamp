import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Detect collision with car
    if car_manager.is_car_hit(player.position()):
        scoreboard.game_over()
        game_is_on = False


    if player.is_player_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start_position()
        car_manager.level_up()

    car_manager.create_car()
    car_manager.move_cars()

screen.exitonclick()
