import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Cross Game")
screen.tracer(0)

turtle = Player()
cars =  CarManager()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()
screen.listen()

screen.onkey(turtle.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)

    cars.create_car()
    cars.move_car()

    for c in cars.cars:
        if c.distance(turtle) < 20:
            game_is_on = False

    if turtle.ycor() == 300:
        turtle.go_inicial()
        scoreboard.score += 1
        scoreboard.update_scoreboard()
        cars.increase_speed()

    screen.update()

game_over = Turtle()
game_over.write("GAME OVER", align="center", font=("Courier", 24, "normal"))
game_over.color("black")
game_over.penup()
game_over.hideturtle()

screen.exitonclick()