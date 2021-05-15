"""
071
Create a list of two sports. Ask the
user what their favourite sport is and
add this to the end of the list. Sort the
list and display it
"""

Sport_List = ["Football","Basketball"]
Input = input("Enter your favourite sport : ")
Sport_List.append(Input)
Sport_List.sort()
print(Sport_List)