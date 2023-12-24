


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):

    end_text = ""           ### stringul in care se va afla textul final ###
    if cipher_direction == "decode":
        shift_amount *= -1          ### daca "decode" => scade cu nr de shift amount ###

    for char in start_text:         ### pt fiecare litera din cuvantul dat ###
        if char in alphabet:            ### daca litera exista in alphabet ###
            position = alphabet.index(char)         ### atunci la ce index se gaseste in alphabet ###
            new_position = position + shift_amount          ### care e pozitia finala dupa shift ###
            end_text += alphabet[new_position]          ### care e litera din alphabet de la pozitia finala ###
        else:
            end_text += char            ### daca nu exista in alphabet sa adauge caracterul asa cum e ###
            print(f"Here is the {cipher_direction}d result: {end_text}.")

should_end = False

while not should_end:

    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
