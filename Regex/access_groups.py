import re

match = re.search(r"(\w+),(\w+)", "one,two,three") # this searches for a group formed of:
        # one word of 1 or more metacharacters, folloed by a comma, and another word of 1 or more metacharacters
print(match.group())  # "one,two"   - the groups() function shows the matching groups
print(match.group(1))   # "one"
print(match.group(2))   # "two"
print(match.group(2, 1)) # ("two", "one")
print(match.group(0)) # "one,two"      - this returns the entire match
print(match[1]) # "one"
print(match[2]) # "two"
print(match.expand("second was '\\2', first was '\\1'"))    # second was 'two', first was 'one'    - this works like an f string
match = re.search("123", "abc,123,xyz")
print(match)