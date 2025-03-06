from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG")
screen.listen()

left_paddle = Paddle()
right_paddle = Paddle()
left_paddle.goto(-350,0)
right_paddle.goto(350,0)

screen.onkey(left_paddle.move_up,"w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up,"Up")
screen.onkey(right_paddle.move_down, "Down")

screen.exitonclick()