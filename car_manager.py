from turtle import Turtle
import random

from TurtleGame.turtle_race import position

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color(random.choice(COLORS))
        self.position = random.randint(-300, 300)
        self.goto(position, -300)