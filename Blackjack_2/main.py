import random

your_cards = []
computer_cards = []
sum_your_cards = 0
sum_computer_cards = 0
should_game_continue = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def stand_win():
    global should_game_continue
    print(f"Your final hand: {your_cards}, final score: {sum_your_cards}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum_computer_cards}")
    print("You win!")
    should_game_continue = False
    print(starting_question)

def stand_lose():
    global should_game_continue
    print(f"Your final hand: {your_cards}, final score: {sum_your_cards}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum_computer_cards}")
    print("You lose.")
    should_game_continue = False
    print(starting_question)

def hit():
    # 2nd random number for player
    next_random_your_card = random.choice(cards)
    your_cards.append(next_random_your_card)

    calculation()

def calculation():
    global sum_your_cards, sum_computer_cards, should_game_continue
    sum_your_cards = 0
    for card in your_cards:
        sum_your_cards += card

    # calculation of the sum for dealer
    sum_computer_cards = 0
    for card in computer_cards:
        sum_computer_cards += card

    if 11 in your_cards and sum_your_cards > 21:
        sum_your_cards = sum_your_cards - 11 + 1
        if sum_your_cards > 21:
            stand_lose()
    elif 11 in your_cards and sum_your_cards == 21:
        if sum_computer_cards == 21:
            print(f"Your cards: {your_cards}, current score: {sum_your_cards}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum_computer_cards}")
            print("It's a draw.")
            should_game_continue = False
            print(starting_question)
        print("Blackjack! You win with a score of 21")
        should_game_continue = False
        print(starting_question)
    elif sum_your_cards > 21:
        should_game_continue = False
        stand_lose()
    else:
        print(f"Your cards: {your_cards}, current score: {sum_your_cards}")
        print(f"Computer's first card is: {computer_cards[0]}")

def hit_or_stand():
    answer = input("Type 'y' to get another card, type 'n' to pass: ")

    if answer == "y":
        hit()
    elif answer == "n":
        if sum_your_cards > sum_computer_cards and sum_your_cards <= 21:
            stand_win()
        else:
            stand_lose()


def draw_cards():
    global sum_your_cards, sum_computer_cards

                 # 1st random number for player
    first_random_card = random.choice(cards)
    your_cards.append(first_random_card)
                 # 1st random number for dealer
    first_random_computer = random.choice(cards)
    computer_cards.append(first_random_computer)

                    # 2nd random number for player
    next_random_your_card = random.choice(cards)
    your_cards.append(next_random_your_card)

                    # 2nd random number for dealer
    next_random_computer = random.choice(cards)
    computer_cards.append(next_random_computer)


while should_game_continue:
    starting_question = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if starting_question == "n":
        should_game_continue = False

    ### the 1st function to run after the while statement should be "draw_cards()" ###
    draw_cards()
    ### 2nd "calculation()"
    calculation()
    ### at this level, after all the functions, there should be the restart question with the if statement
    hit_or_stand()





