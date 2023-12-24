
'''**KWARGS - MANY KEYWORD ARGUMENTS'''

def calculate(n, **kwargs):  ### "n" is a normal positional argument ###
    print(kwargs)
    print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
                # or
    # print(kwargs["divide"])

    n /= kwargs["divide"]
    n *= kwargs["multiply"]
    print(n)

calculate(3, divide=3, multiply=5)

'''**KWARGS - ANOTHER EXAMPLE'''

class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

my_car = Car(make="Nissan", model="Micra")
print(my_car.model)
