from ascii_art import logo

print(logo)
print("Welcome to Treasure Island!")

answer1 = input('You\'re at a crossroad. Where do you go? Type "left" or "right":\n').lower()

if answer1 == "left":
    answer2 = input('You\'ve come to a lake. What do you want to do? Type "swim" or "wait":\n').lower()
    if answer2 == "wait":
        answer3 = input("You arrive at the island. There are 3 doors: blue, red and yellow. Which one do you choose?\n").lower()
        if answer3 == "yellow":
            print("You win!")
        elif answer3 == "red":
            print("You lose. It's a room full of fire.")
        elif answer3 == "blue":
            print("You lose, game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You've been attacked by crocodiles! Game over.")
else:
    print("You fell into a hole. Game over.")