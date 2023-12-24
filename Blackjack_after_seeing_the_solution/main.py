import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "Blackjack! You win!"
    elif computer_score == 0:
        return "Computer has Blackjack. You lose."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Computer went over. You win."
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def game():
    user_cards = []
    computer_cards = []

    for _ in range(2):

        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_is_over = False
    while not game_is_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your current hand: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_is_over = True
        else:
            another_card = input("Do you want a new card? Type 'y' or 'n': ")
            if another_card == "y":
                user_cards.append(deal_card())
            else:
                game_is_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final hand: {computer_score}")
    print(compare_score(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    game()