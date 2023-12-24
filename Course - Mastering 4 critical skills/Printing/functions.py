# def special_multiplication(string):
#     new_cuv = ""
#     for idx, value in enumerate(string):
#         new_cuv += (idx + 1) * value
#     return new_cuv
#
# print(special_multiplication("abcd"))

# def my_max2(a, b):
#     if a > b:
#         return a
#     return b
#
# def my_max3(a, b, c):
#     return my_max2(a, my_max2(b, c))
#
# def my_max4(a, b, c, d):
#     return my_max2(a, my_max3(b, c, d))
#
# def my_max5(a, b, c, d, e):
#     return my_max2(a, my_max4(b, c, d, e))
#
# def my_max6(a, b, c, d, e, f):
#     return my_max2(a, my_max5(b, c, d, e, f))
#
# print(my_max6(5, 3, 8, 2, 10, 3))

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.height * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def get_area(self):
        return self.pi * (self.radius ** 2)

r = Rectangle(2, 5)
print(r.get_area())

c = Circle(5)
print(c.get_area())

class Editor:
    def __init__(self):
        self.rectangle = Rectangle
        self.circle = Circle