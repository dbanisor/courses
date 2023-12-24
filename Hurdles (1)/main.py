

##
     \_o_/
     _/_
    / _ \  _    _    _    _    _    _
_____| |__| |__| |__| |__| |__| |__| |
##

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def one_jump():
    move()
    turn_left()
    move()
    turn_right()
    move()

### functii deja create: turn_left(), move()

turn_right()
move()
turn_left()

for jump in range(6):
    one_jump()