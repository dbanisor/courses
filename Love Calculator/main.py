print("Welcome to the Love Calculator!")
name1 = input("What's your name?\n")
name2 = input("What's their name?\n")
lower_name1 = name1.lower()
lower_name2 = name2.lower()
both_names = lower_name1 + lower_name2

t = both_names.count("t")
r = both_names.count("r")
u = both_names.count("u")
e = both_names.count("e")
l = both_names.count("l")
o = both_names.count("o")
v = both_names.count("v")

sum_true = t+r+u+e
sum_love = l+o+v+e
love_score = int(str(sum_true) + str(sum_love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")