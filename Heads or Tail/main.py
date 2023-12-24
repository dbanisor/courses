import random

#intre 0 si 1 inclusiv#
random_side = random.randint(0, 1)

if random_side == 1:
    print("Heads")
else:
    print("Tails")