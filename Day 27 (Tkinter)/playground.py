# def add(*args):
#     print(args[2])
#     total = 0
#     for n in args:
#         total += n
#     return total
#
# print(add(5, 4, 3, 2, 1))

# def calculate(n, **kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3, multiply=5)
#
# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")
#         self.model = kwargs.get("model")
#         self.color = kwargs.get("color")
#         self.seats = kwargs.get("seats")
#
# my_car = Car(make="Nissan")
# print(my_car.model)


def bar(spam, eggs, toast="yes please!", ham=0):
    print(spam, eggs, toast, ham)

print(bar(1, 2))