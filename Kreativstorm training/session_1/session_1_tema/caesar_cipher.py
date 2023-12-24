'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It encrypts letters by shifting them over by
a certain number of places in the alphabet. We call the length of shift the key. For example, if the key is 3, then A
becomes D, B becomes E, C becomes F, and so on. To decrypt the message, you must shift the encrypted letters in the
opposite direction. This program lets the user encrypt and decrypt messages according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''

import string
from string import punctuation


class CaesarCipher:
    def __init__(self):
        self.alphabet = list(string.ascii_lowercase) * 2
        self.punc_chars = list(punctuation)
        self.enc_or_dec()

    def enc_or_dec(self):
        self.encrypt_or_decrypt = input("Do you want to (e)ncrypt or (d)ecrypt?\n").lower()
        if self.encrypt_or_decrypt != "e" and self.encrypt_or_decrypt != "d":
            print("Invalid choice. Please choose again.")
            return self.enc_or_dec()
        self.choose_key()

    def choose_key(self):
        self.key = int(input("Please enter the key (0 to 25) to use.\n"))
        try:
            if self.key < 0 or self.key > 25:
                print("Invalid choice. Please choose again.")
                return self.choose_key()
        except ValueError:
            print("Invalid choice. Please choose again.")
            return self.choose_key()
        else:
            self.pick_method()

    def pick_method(self):
        if self.encrypt_or_decrypt == "d":
            self.decrypt()
        else:
            self.encrypt()

    def encrypt(self):
        encrypted_message = ""
        message = input("Enter the message to encrypt.\n").lower()
        for char in message:
            if char not in self.alphabet and char not in self.punc_chars and char != " ":
                print("Please try again and use the Latin alphabet.\n")
                self.encrypt()
            elif char in self.punc_chars:
                encrypted_message += char
            elif char == " ":
                encrypted_message += char
            else:
                letter_encrypted = self.alphabet[self.alphabet.index(char) + self.key]
                encrypted_message += letter_encrypted
        print(encrypted_message)

    def decrypt(self):
        decrypted_message = ""
        message = input("Enter the message to decrypt.\n").lower()
        for char in message:
            if char not in self.alphabet and char not in self.punc_chars and char != " ":
                print("Please try again and use the Latin alphabet.\n")
                self.decrypt()
            elif char in self.punc_chars:
                decrypted_message += char
            elif char == " ":
                decrypted_message += char
            else:
                letter_decrypted = self.alphabet[self.alphabet[26::].index(char) - self.key]
                decrypted_message += letter_decrypted
        print(decrypted_message)


x = CaesarCipher()
