from turtle import Turtle, Screen
from random import random

my_scr = Screen()
tim = Turtle("turtle")
tim.pen(pensize=5, speed=10)


def fd():
    tim.forward(10)
    tim.pen(pencolor=(random(), random(), random()))


def right():
    tim.right(5)
    tim.forward(5)
    tim.pen(pencolor=(random(), random(), random()))


def left():
    tim.left(5)
    tim.forward(5)
    tim.pen(pencolor=(random(), random(), random()))


def bd():
    tim.back(10)
    tim.pen(pencolor=(random(), random(), random()))


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def dot():
    tim.dot(20, (random(), random(), random()))


my_scr.listen()
my_scr.onkey(fd, "Up")
my_scr.onkey(right, "Right")
my_scr.onkey(left, "Left")
my_scr.onkey(bd, "Down")
my_scr.onkey(dot, "space")
my_scr.onkey(clear_screen, "c")


my_scr.exitonclick()
