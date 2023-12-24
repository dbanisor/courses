
import random
from art import logo


print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")


def compare(user_answer, random_number):
    if user_answer < random_number:
        return "Too low"
    elif user_answer > random_number:
        return "Too high"
    elif user_answer == random_number:
        return "exact"

### chose a random nb
chosen_nb = random.randint(1, 100)

### choose the difficulty and define the nb of lives
level = {"hard": 5, "easy": 10}
level_chosen = input("Choose a difficulty: Type 'easy' or 'hard': ")
lives = level[level_chosen]


game_is_over = False


while not game_is_over:
    guess = int(input(f"You have {lives} attempts remaining to guess the number.\nMake a guess: "))
    result = compare(user_answer=guess, random_number=chosen_nb)
    if result == "exact":
        lives = 0
        print(f"You got it! The answer was {chosen_nb}.")
        game_is_over = True
    else:
        lives -= 1
        if lives == 0:
            print(result)
            print("You've run our of guesses. You lose.")
            game_is_over = True
        else:
            print(result)
            print("Guess again.")





