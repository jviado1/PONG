from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()
screen.tracer(0)

net = Turtle()
net.color("white")
net.pu()
net.hideturtle()
net.setheading(90)
net.goto(x=0,y=-300)
net.pencolor("white")
for _ in range(0,18):
    net.pd()
    net.forward(20)
    net.pu()
    net.forward(20)


left_paddle = Paddle(-350,0)
right_paddle = Paddle(350,0)

print(left_paddle.position())
print(right_paddle.position())

screen.onkey(left_paddle.move_up,"w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up,"Up")
screen.onkey(right_paddle.move_down, "Down")

game_on = True
while game_on:
    screen.update()


screen.exitonclick()