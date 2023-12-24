import random

names_string = input("Give me everybody's names separated by a comma:\n")

names = names_string.split(", ")
lenght = len(names)-1
random_number = random.randint(0, lenght)

print(f"{(names[random_number])} is going to pay the meal.")