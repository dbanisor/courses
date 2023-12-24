import re

question = "Lovely spam! Wonderful spam!"   # test string
answer = re.search("spam", question) # using the Search method inside the "re" module will return a match object
print(answer)
print(question[7:11])
print(bool(answer))
print(answer.span())    # this will print where is the position of the match in the string
print(answer.start())    # this will print where is the starting position of the match in the string
print(answer.end())    # this will print where is the end position of the match in the string
print(answer.string)    # this will print the string that was matched against

print(re.match("\w{5}", question))  # this searches for 5 word like metacharacters
print(re.fullmatch("spam", question))   # this will look for an expression that matches the entire string
print(re.fullmatch("((\w*\s*)*!)*", question))
print(re.findall("[aeiou][^aeiou]", question)) # findall() doesn't return a match object, it returns a list
print(re.finditer("[aeiou][^aeiou]", question)) # this does the same thing as findall() but returns an iterator instead of a list.
# it's more efficient in memory in case of large nb of matches