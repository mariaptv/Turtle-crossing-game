import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Pong")
screen.tracer(0)

turtle = Player()
for i in range(16):
    car = CarManager()
screen.listen()

screen.onkey(turtle.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
