from random import randint

min_number = int(input('Give a min number: '))
max_number = int(input('Give a max number: '))

if max_number < min_number:
    print('Invalid input, shutting down...')
else:
    rand_number = randint(min_number, max_number)
    print(rand_number)