##

     \_o_/
     _/_
    / _ \  _    _    _    _    _    _
_____| |__| |__| |__| |__| |__| |__| |

##

# functii deja create turn_left(), move(), at_goal()

# INSTRUCTIUNI: Nu stim unde vor fi pereti deci trebuie sa testam
# daca exista wall_in_front() sau nu,
# si daca este wall_in_front() trebuie sa jump_wall() but if there is
# no wall_in_front() we're going to move().
# Si trebuie sa facem asta atata vreme cat we are not at_goal().

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_wall():
    turn_left()
    move()
    turn_right()
    turn_right()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump_wall()
    else:
        move()

