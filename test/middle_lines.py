from turtle import Turtle

middle_line = Turtle()
upper_dotted_line = Turtle()
lower_dotted_line = Turtle()

# Draw the middle line


def draw_middle_line():
    middle_line.penup()
    middle_line.goto(-300, 0)
    middle_line.pendown()
    middle_line.pencolor("white")
    middle_line.hideturtle()
    middle_line.forward(600)


# Draw upper & lower dotted lines
def draw_upper_lower_lines():
    upper_dotted_line.hideturtle()
    upper_dotted_line.penup()
    upper_dotted_line.goto(-300, 3)
    upper_dotted_line.pendown()
    upper_dotted_line.pencolor("white")

    lower_dotted_line.hideturtle()
    lower_dotted_line.penup()
    lower_dotted_line.goto(-300, -3)
    lower_dotted_line.pendown()
    lower_dotted_line.pencolor("white")


    for line in range(30):
        upper_dotted_line.forward(10)
        lower_dotted_line.forward(10)
        upper_dotted_line.penup()
        lower_dotted_line.penup()
        upper_dotted_line.forward(10)
        lower_dotted_line.forward(10)
        upper_dotted_line.pendown()
        lower_dotted_line.pendown()