import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
screen.onkeypress(player.up, "Up")
car_list = []
game_is_on = True
x = 0
while game_is_on:
    x += 1
    screen.update()
    time.sleep(0.1)
    if player.ycor() > 290:
        player.goto(0, -280)
        scoreboard.level_up()
    if x % 6 == 0:
        car_list.append(CarManager())
    for z in range (len(car_list)):
        car_list[z].move()
        if player.distance(car_list[z]) < 25:
            scoreboard.game_over()
            game_is_on = False
        if player.ycor() > 290:

            car_list[z].speed_up()


screen.exitonclick()
