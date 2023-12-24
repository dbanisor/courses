
""" WITHOUT LIST COMPREHENSION """

numbers = [1, 2, 3, 4, 5]
new_list = []

for n in numbers:
    if n < 4:
        add_1 = n + 1
        new_list.append(add_1)

""" WITH LIST COMPREHENSION """

numbers = [1, 2, 3, 4, 5]

new_list = [n + 1 for n in numbers if n < 4]



