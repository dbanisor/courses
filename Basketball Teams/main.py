import turtle
import pandas


screen = turtle.Screen()
screen.title("US Basketball Teams")
image = "US-Capitals-Map-1265x846.gif"
screen.addshape(image)
turtle.shape(image)

# nets_image = "nets.gif"
# screen.register_shape(nets_image)

data = pandas.read_csv("basketball_teams.csv")
all_teams = data.Team.to_list()

guessed_teams = []

while len(guessed_teams) < 27:

    answer_team = (screen.textinput(title=f"{len(guessed_teams)}/27 teams guessed", prompt="Guess another team")).title()

    if answer_team == "Exit":
        missing_teams = []

        for team in all_teams:
            if team not in guessed_teams:
                missing_teams.append(team)
                teams_left = pandas.DataFrame(missing_teams)
                teams_left.to_csv("states_you_forgot.csv")
        break

    if answer_team in all_teams:

        team_data = data[data.Team == answer_team]
        logo = f"image{int(team_data.image)}.gif"
        print(logo)
        screen.register_shape(logo)
        t = turtle.Turtle(shape=logo)
        t.hideturtle()
        t.penup()
        t.goto(int(team_data.x), int(team_data.y))
        t.stamp()
        t.hideturtle()



screen.exitonclick()