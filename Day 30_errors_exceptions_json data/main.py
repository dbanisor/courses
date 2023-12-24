# #-----------------------------FileNotFound---------------------------#
# try: ### first try this ###
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError: ### but if it catches a FileNotFound error do this: ###
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message: ### or if it catches a KeyError do this ###
#     print(f"The key {error_message} does not exist.")
# else: ### if the "try" block suceeds, then to this: ###
#     content = file.read()
#     print(content)
# finally: ### this code will run no matter what will happen (no matter if it catches any errors or not) ###
#     raise TypeError("This is an error that I made up.")


### "raise" = this keyword "raise" allows us to raise our own exceptions ###

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human heights should not be over 3m.")

bmi = weight / height ** 2
print(bmi)





















