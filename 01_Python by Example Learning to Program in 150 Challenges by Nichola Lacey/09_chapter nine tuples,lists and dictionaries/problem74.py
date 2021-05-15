"""
074
Enter a list of ten colours.Ask the user for a starting number between 0 and 4 and an end number
between 5 and 9. Display the list for those colours between the start and end
numbers the user input.
"""
colours = ["greenyellow","mediumblue","beige","yellow","darkmagenta",
          "blueviolet","deeppink","mediumpurple","mediumslateblue","dodgerblue"]

Starting_Number = int(input("Enter a starting number between 0 and 4 : "))
Ending_Number   = int(input("Enter an ending number between 5 and 9  : "))
print(colours[Starting_Number: Ending_Number])