
""" *ARGS - MANY POSITIONAL ARGUMENTS """

""" WITHOUT *ARGS """

def add(n1, n2):
    return n1 + n2

print(add(n1=5, n2=4))

""" WITH *ARGS """

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(5, 4, 10))