"""
082
Show the user a line of text from your favourite poem
and ask for a starting and ending point. Display the
characters between those two points.
"""

the_text = "Magdy loves Merna so much and she is the best girl in the world"
print(the_text)
starting_point = int(input("choose a starting point : "))
ending_point  = int(input("choose a ending point : "))
print(the_text[starting_point : ending_point])
