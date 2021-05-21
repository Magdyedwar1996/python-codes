class PlayerCharacter:
    def __init__(self, name,age ):
        self.Name = name
        self.Age  = age
        print(f"His name is {self.Name} ",end="")
        print(f"and he is {self.Age} years old ")
        print(self)

    def RunFunction(self):
        print("I'am her in the RunFunction!")
        return "She is the best ever"
# this prints the type of the class not the address as it has no address in the Physical Memory
print(PlayerCharacter)

# These objects have Addresses in the physical memory
player1 = PlayerCharacter("Magdy",24)
print(player1)
print("##" * 30+ "\n")

player2 = PlayerCharacter("Merna",15)
print(player2)
print("##" * 30+ "\n")

player3 = PlayerCharacter("Maged",25)
print(player3)
print("##" * 30+ "\n")

player4 = PlayerCharacter("Mayer",26)
print(player4)
print("##" * 30+ "\n")

player5 = PlayerCharacter("Ahmed",50)
print(player5)
print("##" * 30+ "\n")

"""rint(player1.Name)
player3.RunFunction()
"""

"""print("##" * 30)
print(player5.RunFunction())"""