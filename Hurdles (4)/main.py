##
     |
     |
     |              |
     |              |   |       |
_____| |_______|__| |___|_______|____|

##

# functii deja create turn_left(), move(), at_goal()
# front_is_clear(), right_is_clear(), wall_in_front(), wall_on_right()

# INSTRUCTIUNI: Nu stim unde vor fi pereti si nici cat de inalti vor fi.

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_wall():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump_wall()
    else:
        move()
