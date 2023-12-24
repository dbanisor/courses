from turtle import Turtle
import random

COLORS = ["blue", "red", "green", "yellow", "purple", "orange", "magenta"]
STARTING_MOVE_DISTANCE = 10


class CarManagerLeft:
    def __init__(self):
        self.all_cars_left = []
        self.car_speed_left = STARTING_MOVE_DISTANCE

    def create_car_left(self):
        chance = random.randint(1, 6)
        if chance == 6:
            new_car_left = Turtle()
            new_car_left.shape("square")
            new_car_left.penup()
            new_car_left.shapesize(1, 2)
            new_car_left.color(random.choice(COLORS))
            random_y = random.randint(10, 250)
            new_car_left.goto(-300, random_y)
            self.all_cars_left.append(new_car_left)

    def move_cars_left(self):
        for car in self.all_cars_left:
            car.forward(self.car_speed_left)

    def increase_speed_left(self):
        self.car_speed_left += 10