import random

your_cards = []
computer_cards = []
sum_your_cards = 0
sum_computer_cards = 0
should_game_continue = True


def stand_win():
    print(f"Your final hand: {your_cards}, final score: {sum_your_cards}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum_computer_cards}")
    print("You win!")
    should_game_continue = False
    start_game()


def stand_lose():
    print(f"Your final hand: {your_cards}, final score: {sum_your_cards}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum_computer_cards}")
    print("You lose.")
    should_game_continue = False
    start_game()


def start_game():
    starting_question = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if starting_question == "y":
        draw_cards()
    else:
        should_game_continue = False
        return


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


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

    check_for_winner()


def hit():
    # 2nd random number for player
    next_random_your_card = random.choice(cards)
    your_cards.append(next_random_your_card)

    check_for_winner()


def check_for_winner():
    global sum_your_cards, sum_computer_cards, should_game_continue

    # calculation of the sum for player
    sum_your_cards = 0
    for card in your_cards:
        sum_your_cards += card

    # calculation of the sum for dealer
    sum_computer_cards = 0
    for card in computer_cards:
        sum_computer_cards += card

        # should_game_continue = True
    while should_game_continue:

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
                start_game()
            print("Blackjack! You win with a score of 21")
            should_game_continue = False
            start_game()
        elif sum_your_cards > 21:
            should_game_continue = False
            stand_lose()
        else:
            print(f"Your cards: {your_cards}, current score: {sum_your_cards}")
            print(f"Computer's first card is: {computer_cards[0]}")
            answer = input("Type 'y' to get another card, type 'n' to pass: ")

            if answer == "y":
                should_game_continue = True
                hit()
            elif answer == "n":
                if sum_your_cards > sum_computer_cards and sum_your_cards <= 21:
                    stand_win()
                else:
                    stand_lose()


start_game()



