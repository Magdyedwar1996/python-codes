"""
023
Ask the user to type in the first
line of a nursery rhyme and
display the length of the string.
Ask for a starting number and an
ending number and then display
just that section of the text
(remember Python starts counting from 0 and not 1).
"""


nursery_rhyme = input("Enter  nursery rhyme please : " )
length = len(nursery_rhyme)
print("The length of the nursery rhyme is : ",length)
#nursery_rhyme = list(nursery_rhyme)
starting_number = int(input("Enter a  starting and ending number please \n stating one is : "))
ending_number = int(input(" ending one is : "))
print(nursery_rhyme[starting_number:ending_number])


