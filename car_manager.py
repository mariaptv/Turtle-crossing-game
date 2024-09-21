from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.cars= []

    def create_car(self):
        num = random.randint(1,6)
        if num == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            position = random.randint(-250, 250)
            new_car.goto(250, position)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(MOVE_INCREMENT)
            car.speed("fast")