"""
078
Create a list containing the titles of four TV programmes and display
them on separate lines. Ask the user to enter another show and a
position they want it inserted into the list. Display the list again,
showing all five TV programmes in their new positions.
"""

TV_programms = ["Tom and Gerry", "Brother Rashid", "Maher Samuel","Better Life"]
for i in range(4):
    print(TV_programms[i])
print("Enter another TV program and its position : ")
Name = input("Name of TV program : ")
Index =int(input("its position  : "))
TV_programms.insert(Index,Name)
print(TV_programms)
