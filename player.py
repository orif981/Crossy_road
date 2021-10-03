from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.seth(90)
        self.setpos(0, -250)
        self.shape("turtle")

    def move(self):
        self.forward(10)
