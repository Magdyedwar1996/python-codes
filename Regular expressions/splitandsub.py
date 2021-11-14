# ----------------------------------------------------
# -- Regular Expressions => Re Module Split And Sub --
# ----------------------------------------------------
# split(Pattern, String, MaxSplit)  => Return A List Of Elements Split On Each Match
# sub(Pattern, Replace, String, ReplaceCount) => Replace Matches With What You Want
# ----------------------------------------------------
import re

search_one = "I love python"
search_two = "I love python and java"
search_three = "I love python and java and c++"
search_four = "I love python and java and c++ and c#"
# ----------------------------------------------------
string = re.split(" ", search_one)
print(string)
string = re.split(" ", search_two)
print(string)
string = re.split(" ", search_three)
print(string)
string = re.split(" ", search_four)
print(string)

# ----------------------------------------------------
print("=" * 50)
# ----------------------------------------------------
string_two = "how_to_write_a_very-good-article"
string_two = re.split("_|-", string_two)
print(string_two)

# ----------------------------------------------------
print("=" * 50)
# ---------------------------------------------------
mySting = "I love python and java and c++"
print("Before \n ", mySting)
string = re.sub("python", "C", mySting)
print("After \n ", string)
# ----------------------------------------------------
print("=" * 50)
# ---------------------------------------------------

mySting = "I love python and python and python java and c++"
print("Before \n ", mySting)
string = re.sub("python", "C", mySting, 3)  # Replace 3 Times
print("After \n ", string)
# ----------------------------------------------------
print("=" * 50)
# ---------------------------------------------------
