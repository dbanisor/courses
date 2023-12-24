from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from car_manager_left import CarManagerLeft
from scoreboard import Scoreboard
from middle_lines import draw_middle_line, draw_upper_lower_lines


screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Turtle Crossing Game")
screen.bgcolor("black")
screen.tracer(0)

draw_middle_line()
draw_upper_lower_lines()

my_turtle = Player()
car = CarManager()
left_car = CarManagerLeft()
score = Scoreboard()


screen.listen()

screen.onkey(fun=my_turtle.move_up, key="Up")

game_in_on = True
while game_in_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    left_car.create_car_left()
    car.move_cars()
    left_car.move_cars_left()

    # Detect collision with cars on right
    for each_car in car.all_cars:
        if each_car.distance(my_turtle) < 20:
            game_in_on = False
            score.game_over()

    # Detect collision with cars on left
    for each_car in left_car.all_cars_left:
        if each_car.distance(my_turtle) < 20:
            game_in_on = False
            score.game_over()

    # Detect when the turtle goes over the finish line
    if my_turtle.ycor() > 260:
        score.increase_score()
        my_turtle.go_to_start()
        score.update_score()
        car.increase_speed()
        left_car.increase_speed_left()



screen.exitonclick()