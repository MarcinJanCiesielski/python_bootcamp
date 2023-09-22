import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self) -> None:
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT

    def move_cars(self):
        for car in self.cars:
            car.backward(self.move_distance)

    def is_car_hit(self, position):
        for car in self.cars:
            if car.distance(position) < 20:
                return True
        return False
