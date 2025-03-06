from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_position,y_position):
        super().__init__()
        self.goto(x_position,y_position)
        self.shape("square")
        self.shapesize(1,6)
        self.setheading(90)
        self.color("white")
        self.pu()

    def move_up(self):
        self.forward(40)

    def move_down(self):
        self.back(40)