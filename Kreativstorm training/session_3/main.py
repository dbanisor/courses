# try:
#     with open(r"C:\Users\Denis\Desktop\new_file.txt") as f:
#         content = f.read()
#         print(content.upper())
# except Exception as exc:
#     print("File does not exist", exc)



# with open(r"C:\Users\Denis\Desktop\mbox-short.txt") as f:
#     lst = []
#     content = f.readlines()
#     # print(content)
#     for i in content:
#         j = i.split(" ")
#         print(j, end="---")
#         try:
#             if "From" in j[0]:
#                 if "@" in j[1]:
#                     lst.append(j[1])
#             elif "From" in j[1]:
#                 if "@" in j[2]:
#                     lst.append(j[2])
#         except IndexError:
#             pass
#
# print(lst)

# try:
#     with open(r"C:\Users\Denis\Desktop\mbox-short.txt") as f:
#         count = 0
#         for line in f:
#             if line.startswith("From "):
#                 words = line.split()
#                 print("Sender:", words[1])
#                 count += 1
#         print("Total number of lines:", count)
# except FileNotFoundError:
#     print("File not found!")

import re

txt = "The rain in Spain"

x = re.findall('ai', txt)
print(x)

y = re.search('ai', txt)
print(y)