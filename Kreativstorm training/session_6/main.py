'''1. Create a decorator @validate_input that checks if the arguments passed to a function are all integers.
If any argument is not an integer, it should raise a ValueError. Decorate a function with this decorator and call it.'''

# def validate_input(func):
#     def inner(*args):
#         for i in args:
#             if not isinstance(i, int):
#                 raise ValueError("args must be int")
#         return func(*args)
#     return inner
#
# @validate_input
# def func_to_be_decorated(*args):
#     return args
#
# print(func_to_be_decorated(3, "9", 3))

'''2. Create a parameterized decorator @repeat(n) that repeats the execution of a function n times. Then, decorate a 
function with this decorator and call it.'''

# def repeat(func):
#     def inner(n):
#         for i in range(n):
#             func(n)
#         return
#     return inner
#
# @repeat
# def print_hello(n):
#     print("Hello")
#
# a = print_hello(3)
# -------------------------------------------
# def repeat(n):
#     def decorator(func):
#         def inner(*args, **kwargs):
#             for _ in range(n):
#                 func(*args, **kwargs)
#         return inner
#     return decorator
#
#
# @repeat(5)
# def print_to_repeat(text):
#     print(f"{text}")
#
# print_to_repeat("Hello World!")

'''1. Write a generator function range_generator(start, end, step) that generates a sequence of numbers from start to 
end with a given step. Then, use this generator to find and print all multiples of 3 from 10 to 30 with a step of 5.'''

# def range_generator(start, end, step):
#     for i in range(start, end, step):
#         while start <= end:
#             yield start
#             start += step
#
# for num in range_generator(10, 30, 5):
#     if num % 3 == 0:
#         print(num)

'''2. You want to create a decorator that can modify the behavior of generator functions. Write a Python decorator 
@uppercase_generator that takes a generator function as input and yields the uppercase version of each generated value. 
Then, decorate a generator function of your choice with @uppercase_generator and demonstrate how it can be used to 
generate and print uppercase strings from the generator.'''

def uppercase_generator(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        for value in gen:
            yield value.upper()
    return wrapper

@uppercase_generator
def fruits():
    fruits = ["apple", "cherry", "banana"]
    for fruit in fruits:
        yield fruit

fruits_generated = fruits()

for fruit in fruits_generated:
    print(fruit)