print("Welcome to the tip calculator!")
bill = float(input("What's the total bil?? \n"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
nb_of_people = int(input("How many people to split the bill?\n"))

bill_per_person = "{:.2f}".format((bill + bill * (tip / 100)) /nb_of_people)
print(f"Each person should pay: $ {bill_per_person}")