from turtle import Turtle, Screen
import random

color_list = [(232, 227, 214), (218, 218, 223), (108, 110, 127), (214, 153, 89), (140, 141, 152), (196, 59, 24), (227, 214, 103), (234, 217, 226), (180, 159, 39), (99, 108, 177), (211, 145, 178), (29, 46, 27), (27, 26, 70), (199, 18, 5), (37, 40, 18), (227, 167, 198), (221, 81, 52), (43, 45, 106), (126, 84, 96), (217, 75, 99), (232, 173, 161), (87, 100, 90), (182, 184, 213), (188, 14, 21), (153, 165, 157), (222, 206, 23), (48, 27, 50), (73, 72, 38), (51, 72, 53), (182, 198, 185), (115, 134, 125), (175, 199, 204), (117, 131, 134), (47, 70, 73)]

tim = Turtle()
tim.hideturtle()

screen = Screen()
screen.colormode(255)

tim.penup()
tim.setposition(-200.00, -200.00)


def draw_horizontally(distance, x_dots):
    for _ in range(x_dots):
        new_color = random.choice(color_list)
        tim.dot(20, new_color)
        tim.forward(distance)


def go_up_on_y(distance):
    tim.setx(-200)
    tim.sety(distance)


y_scale = [-150, -100, -50, 0, 50, 100, 150, 200, 250, 300]


for nb in y_scale:
    draw_horizontally(50, 10)
    go_up_on_y(distance=nb)











screen.exitonclick()