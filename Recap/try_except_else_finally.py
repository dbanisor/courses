
'''
TRY = something that might cause an exception
EXCEPT = do this if there was an exception
ELSE = do this if there were no exceptions
FINALLY = do this no matter what happens
'''

try:
    file = open("example_files/a_file.txt")   ### FileNotFound Error ###
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])    ### KeyError #####
except FileNotFoundError:
    file = open("example_files/a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The {error_message} key doesn't exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")

''' RAISE YOUR OWN ERROR'''

try:
    file = open("example_files/a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("example_files/a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The {error_message} key doesn't exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error I made up.")   ### RAISING MY OWN EXCEPTION #####

''' RAISE YOUR OWN ERROR - another example'''

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3.00:
    raise ValueError("I doubt you're that tall...")

bmi = weight / height ** 2
print(bmi)