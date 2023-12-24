from turtle import Turtle

LEVEL_POSITION = (-280, 260)
FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self. penup()
        self.color("white")
        self.hideturtle()
        self.goto(LEVEL_POSITION)
        self.update_score()

    def increase_score(self):
        self.clear()
        self.level += 1

    def update_score(self):
        # self.clear()
        self.write(arg=f"Level: {self.level} ________________________", align="left", font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font = FONT)

