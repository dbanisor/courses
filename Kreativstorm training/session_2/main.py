# import random
#
# print(dir(random))
# def d():
#     """
#     A doc string! accessible with f.__doc__
#     """
#     print("Hi!")
#
#
# '''
# LEGB
# Local, Enclosing, Global, Built-in
# '''
#
# x = 2
#
# def (f):
#     x = 10
#     print(x)
# f()
# print(x)




'''
1. Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters
(hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
'''

# def salary(hours, rate):
#     try:
#         if hours > 40:
#             ot = hours - 40
#             ot_pay = ot*(rate/2 + rate)
#             return 40 * rate + ot_pay
#         else:
#             return rate * hours
#     except ValueError:
#         print('You must only add numbers.')
#         salary(hours, rate)
#     else:
#         return hours * rate
#
# print(salary('i', 10))
#---------------------------------------JJ
# def computepay(hours, rate):
#     if(hours <= 40):
#         return hours*rate
#     else:
#         return 40*rate + (hours-40)*rate*1.5
# try:
#      hours = float(input("Enter hours: "))
#      rate = float(input("Enter rate: "))
#      if hours < 0 or rate < 0:
#         raise ValueError("Hours and rate must be positive numbers.")
#      pay = computepay(hours, rate)
#      print(f"Pay: {pay}")
# except ValueError as e:
#     print(f"Error: {e}")

'''
2. Rewrite the grade program from the previous chapter using
a function called computegrade that takes a score as its parameter and
returns a grade as a string.

Score   Grade
>= 0.9  A
>= 0.8  B
>= 0.7  C
>= 0.6  D
< 0.6   F
'''
# def computegrade(score):
#     if score < 0:
#         return "Invalid"
#     elif score < 0.6:
#         return "F"
#     elif score < 0.7:
#         return "D"
#     elif score < 0.8:
#         return "C"
#     elif score < 0.9:
#         return "B"
#     elif score >= 0.9:
#         return "A"
#
# try:
#     score = float(input("Enter score here: "))
#     if score < 0 or score > 1.0:
#         raise ValueError("Score must be between 0 and 1.0.\n Enter the score again.")



#------------------------berru
# def computegrade(score):
#     if score >= 0.9:
#         return 'A'
#     elif score >= 0.8:
#         return 'B'
#     elif score >= 0.7:
#         return 'C'
#     elif score >= 0.6:
#         return 'D'
#     else:
#         return 'F'
#
# try:
#     score = float(input("Enter a score between 0.0 and 1.0: "))
#
#     if score < 0.0 or score > 1.0:
#         raise ValueError("Score must be between 0.0 and 1.0.")
#     if not isinstance(score,float):
#         raise ValueError("Score must be a number")
#
#
#     grade = computegrade(score)
#     print(f"Grade: {grade}")
# except ValueError as e:
#     print(f"Error: {e}")
#-----------------------------------------JJ
# def computegrade(score):
#   if score >= 0.9:
#     return 'A'
#   elif score >= 0.8:
#     return 'B'
#   elif score >= 0.7:
#     return 'C'
#   elif score >= 0.6:
#     return 'D'
#   else:
#     return 'F'
#
# try:
#     score = float(input("Enter a score between 0.0 and 1.0: "))
#     if score < 0.0 or score > 1.0:
#         raise ValueError("Score must be between 0.0 and 1.0")
#     grade = computegrade(score)
#     print(f"Grade: {grade}")
# except ValueError as e:
#   print(f"Error: {e}")
'''
# problem
print('Good morning!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')
print('Good afternoon!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')
print('Good evening!')
print('How are you feeling?')
feeling = input()
print('I am happy to hear that you are feeling ' + feeling + '.')
'''
# import random
#
# def my_func():
#     def inner_func():
#         for i in range(3):
#             lst = ['morning', 'afternoon', 'evening']
#             print(f'Good {random.choice(lst)}!')
#             print('How are you feeling?')
#             feeling = input()
#             print('I am happy to hear that you are feeling ' + feeling + '.')
#     return inner_func()
#
# print(my_func())


#------------------------------------------------------------

# def x(*args):
#     for arg in args:
#         print(arg)
#
# x('adsf', 'hdskj', 6)

#------------------------------------------------------------

# def my_func(*args, **kwargs):
#     print("args: ", args)# tuple
#     print("kwargs: ", kwargs)# dictionary
#
# my_func('This', 'is', 'demo', first="This", mid="is", last="demo.")
#------------------------------------------------------------
#
# fruits = ['apple', 'banana', 'cherry']
#
# for i in fruits:
#     if i == 'banana':
#         continue
#     print(i)
#--------apple, banana



def func(*args):
    print(f'{args} ----\n')

func("apple")
func("banana", "kljsfklifeaij")
func("banana", "kljsfklifeaij", "this is a message 401")

