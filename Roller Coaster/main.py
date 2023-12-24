print("Welcome to the Roller coaster!")

height = int(input("What's your height in cm?\n"))

if height >= 120:
    print("You can ride!")
    age = int(input("What is you age?\n"))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $8.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller.")