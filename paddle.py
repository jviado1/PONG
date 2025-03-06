from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,6)
        self.setheading(90)
        self.color("white")
        self.pu()

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.back(20)