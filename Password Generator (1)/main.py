import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))


count_letters = 0
letters_list = []
for letter in letters:
    rand_char = random.choice(letters)
    count_letters += 1
    if count_letters <= nr_letters:
        letters_list.append(rand_char)

count_numbers = 0
numb_list = []
for number in numbers:
    rand_num = random.choice(numbers)
    count_numbers += 1
    if count_numbers < nr_numbers:
        numb_list.append(rand_num)

count_symb = 0
symb_list = []
for symb in symbols:
    rand_symb = random.choice(symbols)
    count_symb += 1
    if count_symb <= nr_symbols:
        symb_list.append(rand_symb)


total = nr_letters+nr_symbols+nr_numbers

count_items = 0
items_list = letters_list + numb_list + symb_list
random.shuffle(items_list)

final_list_str = ""
for final_item in items_list:
    final_list_str += str(final_item)
print(f"Here is your password: {final_list_str}")
