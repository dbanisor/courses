from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backwards():
    tim.back(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()


screen.onkey(fun=forward, key="w")

screen.onkey(fun=backwards, key="s")

screen.onkey(fun=counter_clockwise, key="a")

screen.onkey(fun=clockwise, key="d")

screen.onkey(fun=clear_screen, key="c")
















screen.exitonclick()