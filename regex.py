# regex exist as a module
import re
# it stands for regular expressions : sequence of characters that form a search pattern
# use of regex: to check if strings contain a pattern

text = "It is quite sunny today"
# searchregex method: returns a match object if there is any match in string
# ^ indicates a start :eg if text starts with sunny, it starts with it
# $ indicates end with
# * indicates zero or more occurrences
# . indicates any character
# signs above are called metacharacters : characters with special meanings
x = re.search("^It.*", text)
print(x)

# find all : returns a list containing possible matches
x = re.findall("sunny",text)
print(x)

# split : returns a list where the string has been split at each match
x = re.split("\s", text)
print(x)

# sub : replaces the search term with ur own word of choice
x = re.sub("\s", "4", text)
print(x)

# match : equivalent to search