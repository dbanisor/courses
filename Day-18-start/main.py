from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("turquoise3")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(nb_of_sides):
    angle = 360 / nb_of_sides
    for _ in range(nb_of_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)




screen = Screen()
screen.exitonclick()
