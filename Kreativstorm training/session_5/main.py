'''CLASSES'''

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"I am {self.name} {self.age} old"
#
# p1 = Person("John", 20)
# print(p1)

# class MyC:
#     def __init__(self):
#         self.__myvar = 42
#
#
# ponj = MyC()
# print(ponj._MyC__myvar)
#
# print(MyC.__dict__)

'''1. Create a Car class with attributes make, model, and year. Implement a method display_info that prints information
 about the car, such as "Make: Toyota, Model: Camry, Year: 2022."'''

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def display_info(self):
#         return f"Make: {self.make}, Model: {self.model}, Year: {self.year}."
#
#
# car1 = Car('Toyota', 'Camry', 2022)
# print(car1.display_info())

'''2. Create a Circle class with an attribute radius. Implement methods to calculate and return the area and circumference of the circle.'''
# from math import pi
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def circle_area(self):
#         return pi*(self.radius**2)
#     def circle_circumference(self):
#         return 2*pi*self.radius
#
# r = Circle(5)
# print(r.circle_area())
# print(r.circle_circumference())


############################# DATACLASSES ######################################

# from dataclasses import dataclass
#
# @dataclass
# class Person:
#     name: str = "Jane"
#     age: int = 30
#     height: float = 1.80
#
# p1 = Person()
# print(p1)
#
# person = Person('john', 20, 1.50)
# print(type(person))
# print(type(Person()))


from dataclasses import dataclass

@dataclass(order=False)
class Person():
    name: str
    age: int
    height: float

joe = Person('Joe', 25, 1.85)
mary = Person('Mary', 43, 1.85)
