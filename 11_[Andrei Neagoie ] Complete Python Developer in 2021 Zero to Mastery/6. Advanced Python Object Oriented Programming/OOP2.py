class PlayerCharacter:

    membership = True
         # this is Class Object Attribute
         # Class Object Attribute can be accessed through the "Class.Attribute" or "Object.Attribute"



         # [Constructor] or [init function] or [Dunder function ]
    def __init__(self, name,age ):
        # this is object attribute
        self.Name = name
        self.Age  = age
        print(f"His name is {self.Name} ",end="")
        print(f"and he is {self.Age} years old ")
        print(self)


        # this Object methos is to show that membership is accessed through [Object] and[class]
    def Print(self):
        print(PlayerCharacter.membership)
        print(self.membership)
        print("\\"*50)



        # Object method
    def RunFunction(self):
        print("I'am her in the RunFunction!")
        return "She is the best ever"
# this prints the type of the class not the address as it has no address in the Physical Memory
print(PlayerCharacter)

# This object has Address in physical memory
player1 = PlayerCharacter("Magdy",24)
#print(player1)
print("##" * 30+ "\n")


player1.Print()
player1.Print()