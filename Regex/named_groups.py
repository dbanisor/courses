import re

print(re.search("\w+,", "one,two"))    # looking for a metacharacter 1 or more times and a comma
# "one"
print(re.search("\\w+,", "one,two"))
# "one"
print(re.search("\w+\\two", "one\\two"))
# "None"
print(re.search("\w+\\\\two", "one\\two"))
# "one\\two"


words = "I live at 123 Somewhere Street."
match = re.search("(?P<digits>\d+)", words) # ?P - indicates a naming, <indicates the name of the group>, \d+ - indicates digits one or more
print(match)
# "123". Those digits are inside the named group (digits)