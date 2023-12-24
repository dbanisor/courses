from art import logo, vs
from game_data import data
import random
import os

def clear():
    os.system('cls')

def pick_an_item():
    ##### Pick 2 random items from list of data
    pick_item = random.randint(0, len(data) - 1)
    return pick_item


def compare(first_item, second_item):
    ##### Compare function between item A and item B #####
    if first_item == second_item:
        first_item = random.randint(0, len(data) - 1)
    first_item_followers = int(data[first_item]["follower_count"])
    # print(f"First item has {first_item_followers} followers.")
    second_item_followers = int(data[second_item]["follower_count"])
    # print(f"Second item has {second_item_followers} followers.")
    if first_item_followers > second_item_followers:
        return "A"
    else:
        return "B"


def print_items(first_item, second_item):
    first_item_name = data[first_item]["name"]
    first_item_description = data[first_item]["description"]
    first_item_country = data[first_item]["country"]

    print(f"Compare A: {first_item_name}, a {first_item_description}, from {first_item_country}.")

    second_item_name = data[second_item]["name"]
    second_item_description = data[second_item]["description"]
    second_item_country = data[second_item]["country"]

    print(vs)

    print(f"Against B: {second_item_name}, a {second_item_description}, from {second_item_country}.")


##### Compare function between user's input and result from first compare function
def compare_with_answer(largest_acct, user_input):
    # global score
    # score = 0
    if largest_acct == user_input:
        # score += 1
        return "Correct"
    ####      largest becomes A and we pick another random item for B
    else:
        return


def game():
    game_is_over = False
    score = 0

    print(logo)

    item_a = pick_an_item()
    while not game_is_over:
        # print(f"First item is at number {item_a}")
        item_b = pick_an_item()
        # print(f"Second item is at number {item_b}")

        largest = compare(first_item=item_a, second_item=item_b)
        # print(largest)

        print_items(first_item=item_a, second_item=item_b)
        guess = input("Who has more followers? Type 'A' or 'B': ")

        answer = compare_with_answer(largest_acct=largest, user_input=guess)

        ##### acest IF ar trebui inlocuit cu un WHILE #####
        if answer == "Correct":
            score += 1
            clear()
            print(logo)
            print(f"You're right! Current score: {score}.")
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game_is_over = True

        item_a = item_b


game()