import re
string = "search inside of this text please!"
print('search' in string)

output = re.search("text",string)
print(output)

# this function to get the location of the text in the string
print(output.span())

# this function to get the beginning of the text in the string
print(output.start())

# this function to get the end of the text in the string
print(output.end())

# this function to get the text in the string
print(output.group())

# this function to get the type of the text in the string
print(type(output))

print("#"*50)

#///////////////////////////////////////////////////////////////////////////////////

text = "I love merna so much and she is the best girl in the world ," \
       " and she is still the best one in my eyes  "

pattern = re.compile("best")
print(type(pattern))
OUTPUT = pattern.search(text)
print(OUTPUT.group())


b = pattern.findall(text)
print(b)