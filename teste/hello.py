''' 1. Square Numbers:
Write a lambda function that squares a given number and then use map to square each element in a list of numbers.

Example:
Input: [1, 2, 3, 4, 5]
Output: [1, 4, 9, 16, 25]'''

# input1 = [1, 2, 3, 4, 5]
# print(list(map(lambda x: x**2, input1)))


''' 2. Filter Even Numbers:
Write a lambda function that checks if a number is even and then use filter to get a list of even numbers from a list.

Example:
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Output: [2, 4, 6, 8]'''

# input1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(filter(lambda x: x % 2 == 0, input1)))


''' 3. Sort by Last Name:
Given a list of names in the format "First Name Last Name," use sorted and a lambda function to sort the list by last name.

Example:
Input: ["Alice Smith", "Bob Johnson", "Eva Williams", "David Lee"]
Output: ["David Lee", "Bob Johnson", "Alice Smith", "Eva Williams"]'''

# input1 = ["Alice Smith", "Bob Johnson", "Eva Williams", "David Lee"]
# print(sorted(input1, key=lambda x: x.split(' ')[1]))


''' 4. Find Maximum Value:
Use max and a lambda function to find the maximum value in a list of tuples. Each tuple contains a name and an associated age.

Example:
Input: [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
Output: ("Charlie", 35)'''

# input1 = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
# print(max(input1, key=lambda x: x[1]))


''' 5. Calculate Average:
Write a lambda function that calculates the average of three numbers and use it to find the average of a list of triples (each triple is a tuple of three numbers).

Example:
Input: [(10, 20, 30), (5, 15, 25), (8, 18, 28)]
Output: [20.0, 15.0, 18.0]'''

# input1 = [(10, 20, 30), (5, 15, 25), (8, 18, 28)]
# print(list(map(lambda x: sum(x)/len(x), input1)))

''' 6. Remove Duplicates:
Use filter and a lambda function to remove duplicate elements from a list.

Example:
Input: [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]'''
# lst = []
# input1 =[1, 2, 2, 3, 4, 4, 5]
# list(filter(lambda x: lst.append(x) if x not in lst else False, input1))
# print(lst)

''' 7. Find Palindromes:
Write a lambda function that checks if a given word is a palindrome (reads the same forwards and backwards) and use it to filter a list of words.

Example:
Input: ["racecar", "python", "level", "hello", "deified"]
Output: ["racecar", "level", "deified"]'''

# input1 = ["racecar", "python", "level", "hello", "deified"]
# print(list(filter(lambda x: x == x[::-1], input1)))