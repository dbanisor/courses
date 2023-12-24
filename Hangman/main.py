import random
from hangman_art import logo, stages
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"


used_letters = ''

# ask for user input
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    if guess in display:
        print(f"You've already guessed {guess}")

    if guess not in used_letters:
        used_letters += guess

    print(f"Used letters: {used_letters}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(f"\nYou guessed {guess}. You have {lives} tries left.")

    # Check if user is wrong.
    if guess not in chosen_word:

        lives -= 1
        print(f"\nYou guessed {guess}, that's not in the word. You have {lives} tries left.")
        if lives == 0:
            end_of_game = True
            print("GAME OVER. You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print(f"You guessed the word {chosen_word}! You win!")


    print(stages[lives])