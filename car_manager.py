from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def create_cars(self, random1):

        if random.randint(0, random1) == 0:
            car = Turtle()
            car.pu()
            car.shape("square")
            car.setpos(320, random.randint(-160, 230))
            car.color(random.choice(COLORS))
            car.shapesize(1, 2)
            car.seth(180)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)

    def check(self, turtle):
        for car in self.cars:
            if car.xcor() < -320:
                self.cars.remove(car)
            if car.distance(turtle) < 27:
                return False
        return True

    def clear(self):
        for car in self.cars:
            car.hideturtle()
        self.cars = []
