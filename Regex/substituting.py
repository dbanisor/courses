import re

content = "My favorite numbers are 13 and 42"
print(re.sub(r"\d+", "#", content))
# My favorite numbers are # and #

content = "My favorite numbers are 13 and 42"
print(re.sub(r"\d+", "#", content, count=1))    # this limits the nb of substitutes
# My favorite numbers are # and 42
