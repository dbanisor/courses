student_heights = input("Input a list of student heights: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

#this calculates the sum#
total_height = 0
for height in student_heights:
    total_height += height

#this calculates the lenght#
number_of_students = 0
for student in student_heights:
    number_of_students += 1

#this calculates the average#
average_height = total_height / number_of_students
print(int(average_height))