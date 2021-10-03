import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, random1

screen = Screen()
loc = -160
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

finish_line = Turtle()
finish_line.pu()
finish_line.shape("square")
finish_line.setpos(0, 260)
finish_line.shapesize(0.1, 50)

screen.onkeypress(player.move, "w")
game_is_on = True
while game_is_on:

    if random1 == 0:
        scoreboard.won()
        break
    time.sleep(0.1)
    screen.update()
    cars.create_cars(random1)
    cars.move()
    if not cars.check(player):
        scoreboard.game_over()
        screen.update()
        break
    if player.ycor() > finish_line.ycor():
        cars.clear()
        player.setpos(0, -250)
        random1 -= 1
        if random1 != 8:
            scoreboard.rewrite()

screen.exitonclick()
