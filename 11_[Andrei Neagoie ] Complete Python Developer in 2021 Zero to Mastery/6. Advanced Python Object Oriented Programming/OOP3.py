class PlayerCharacter:
    
    membership = True
         # this is Class Object Attribute
         # Class Object Attribute can be accessed through the "Class.Attribute" or "Object.Attribute"

         # [Constructor] or [init function] or [Dunder function ]
    def __init__(self, name,age):
        # this is object attribute
        self.Name = name
        self.Age  = age
        print(f"His name is {self.Name} ",end="")
        print(f"and he is {self.Age} years old ")
        print(self)


    # this is class method like the class Attribute
    @classmethod
    def adding_numbers(cls , num1 , num2):
        return (num1 + num2)

    # this is the same as classmethod but with little difference
    @staticmethod
    def Multipling_numbers( num1, num2):
        return (num1 * num2)

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
while 1 :
    print("Enter two number to add : ")
    num1 = int(input())
    num2 = int(input())

    print("way one \n Calling the[class method] through the Class:", PlayerCharacter.adding_numbers(num1,num2))
    print("**" * 30)

    print("way two \n Calling the[class method] through the object",player1.adding_numbers(num1,num2))
    print("**" * 30)

    print("Enter two number to multiply : ")
    num3 = int(input())
    num4 = int(input())
    print("way one \n Calling the[Static method] through the class ",PlayerCharacter.Multipling_numbers(num3,num4))
    print("**" * 30)

    print("way two \n Calling the[Static method] through the object ",player1.Multipling_numbers(num3,num4))
    print("**" * 30)

"""
player1.Print()
player1.Print()
"""
              ###  IMPORTANT NOTE ###
# as the Object method takes [self] as a parameter
# the class method takes [cls] as a parameter