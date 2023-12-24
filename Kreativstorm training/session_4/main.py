# List comprehension

# lst = [i**2 for i in [1, 2, 3]]
# print(lst)

# lst = [i for i in range(11) if i % 2 == 0]
# print(lst)

# combs = []
# for x in combs:
#     for y in combs:
#         if x != y:
#             combs.append((x, y))


# combs = [[x, y] for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

# matrix = []

# for i in range(3):
#     matrix.append([])
#
#     for j in range(5):
#         matrix[i].append(j)


# matrix = [[j for j in range(5)] for i in range(3)]
# print(matrix)

# lis = ['even' if i % 2 == 0 else 'odd' for i in range(8)]
# print(lis)

# lis = [num for num in range(100) if num % 5 == 0 if num % 10 == 0]
# print(lis)

'''1. Write a list comprehension to extract all the vowels (lowercase) from a given sentence.'''

# vowels = 'aeiou'
#
# answer = input("Give a sentence: ")
#
#
# output = [i for i in answer if i in vowels]
#
# print("".join(output))


'''2. Write a list comprehension to flatten a nested list. For example, turn [[1, 2, 3], [4, 5], [6]] into [1, 2, 3, 4, 5, 6].'''
# lst = [[1, 2, 3], [4, 5], [6]]
# new = [j for i in lst for j in i]
# print(new)
######################### lambda functions ##########################'/'##

# lambda parameter(s): expression

# x = lambda a, b: a + b
# print(x(5, 5))

# def myfunc(n):
#     def doubler(a):
#         return a * n
#     return doubler
#
# mydoubler = myfunc(2)
#
# result = mydoubler(11)
# print(result)

# def myfunc(n):
#     return  lambda a: a * n
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
#
# result = mydoubler(11)
# result2 = mytripler(11)
# print(result)
# print(result2)


# str_1 = 'Welcome'
#
# rev_upper = lambda string: string.upper()[::-1]
# print(rev_upper(str_1))

# def double(x):
#     return x * 10
#
# is_even = []
#
# for x in range(1, 5):
#     result = double(x)
#     is_even.append(result)

# print([(lambda arg=x: arg * 10)() for x in range(1, 5)])

#################### filter function
#
# li = [5, 7, 22, 65, 77, 45, 88, 99, 61]
#
# final_list = list(filter(lambda x: (x%2==0), li)) # it eliminates the need of a for loop
# print(final_list)

# ages = [13, 90, 17, 87, 21, 5]
#
# adults = list(filter(lambda age: age > 18, ages))
#

#################### map function

# li = [5, 7, 22, 97, 53, 62, 77, 23, 73, 61]
#
# final_list = list(map(lambda x: x*2, li))
# print(final_list)

# animals = ['dog', 'cat', 'parrot']
#
# upp_animals = list(map(lambda animal: animal.upper(), animals))
# print(upp_animals)

from functools import reduce
#
# li = [5, 8, 10, 20, 50, 100]
#
# sum_li = reduce(lambda x, y: x + y, li)
#
# print(sum_li)

'''1. Write a lambda function that you can use as the key argument in the sorted() function to sort the list of tuples 
\based on the ages in ascending order. After sorting, print the sorted list.'''

# people = [("Alice", 25), ("Bob", 30), ("Charlie", 22), ("David", 35)]
#
# sorted_people = sorted(people, key=lambda x: x[1])
#
# print(sorted_people)

'''2. You are given a list of numbers. Your task is to write Python code that calculates the average of these numbers 
using the reduce() function from the functools module and a lambda function.'''

# li = [5, 8, 10, 20, 50, 100]
#
# avg = reduce(lambda x, y: x + y, li) / len(li)
# print(avg)

#################### tuples

x = ('apple', 'banana', 'cherry', 'kiwi', 'melon', 'mango')

# updating tuples

# y = list(x)
# y[1] = 'pear'
# x = tuple(y)
# print(x)

# y = list(x)
# y.append('pear')
# x = tuple(y)
# print(x)

##############apending tuples with other tuples

# y = ('orange',)
# x += y
# print((x))
##########
# fruits = ('apple', 'banana', 'cherry')
# green, yellow, red = fruits
# print(green)
# print(yellow)


# fruits = ('apple', 'banana', 'cherry', 'kiwi', 'melon', 'mango')
# green, yellow, *red = fruits
# print(green)
# print(yellow)
# print(*red)


#################### sets

# this_set = {'apple', 'banana', 'cherry', 'apple'}
# print(id(this_set))
# this_set.add('xyz')
# print(id(this_set))

# set_1 = {"a", "b", "c"}
# set_2 = {"d", "e", "f"}
#
# set_1.update(set_2)
# print(set_1)

# set_1 = {"a", "b", "c"}
# set_2 = {"d", "e", "f"}
#
# set3 = set_1.union(set_2)
# set4 = set_1.intersection(set_2)

#################### FROZEN SET

# fs = frozenset([1, 2, 3, 4, 4])
#
# print(fs)


fs1 = frozenset([1, 2, 3])
fs2 = frozenset([2, 3, 4])

union_results = fs1 | fs2
intersection = fs1 & fs2
difference = fs1 - fs2

print(union_results)
print(intersection)
print(difference)
