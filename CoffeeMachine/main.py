MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: $0')


def enough_ingredients(user_choice):

    for ingredient in MENU[user_choice]["ingredients"]:
        if MENU[user_choice]["ingredients"][ingredient] > resources[ingredient]:
            return f"Sorry, there is not enough {ingredient}"
        else:
            return "yes"


def enough_money(money, user_choice):
    if MENU[user_choice]["cost"] > money:
        return "Sorry, not enough money."
    else:
        return "yes"


def drink(user_choice):
    if user_choice not in MENU:
        print("Not in the menu.")
    else:
        for ingredient in MENU[user_choice]["ingredients"]:
            resources[ingredient] -= MENU[user_choice]["ingredients"][ingredient]
            #if resources[ingredient] < 0:
                #print(f"Not enough {ingredient}.")
    print(f"Here's your {user_choice}! Enjoy!")


should_continue = True


while should_continue:
    answer = input("What would you like? (espresso/latte/cappuccino): ")

    if answer in MENU:
        if enough_ingredients(user_choice=answer) == "yes":
            quarters = (float(input("How many quarters?: ")) * 0.25)
            dimes = (float(input("How many dimes?: ")) * 0.10)
            nickles = (float(input("How many nickles?: ")) * 0.05)
            pennies = (float(input("How many pennies?: ")) * 0.01)

            total_money = float("{:.2f}".format(quarters + dimes + nickles + pennies))

            if enough_money(money=total_money, user_choice=answer) == "yes":
                drink(user_choice=answer)
                if total_money > MENU[answer]["cost"]:
                    change = "{:.2f}".format(total_money - MENU[answer]["cost"])
                    print(f"Here's ${change} in change.")
            else:
                print(enough_money(money=total_money, user_choice=answer))
                should_continue = False
                print(f"Here's ${total_money} back.")
        else:
            print(enough_ingredients(user_choice=answer))
    else:
        report()




