class Person :
    def __init__(self, name , age):
        self.name = name
        self.age = age

        print("the self is :", self)
        print("The name of the fist person is : ",name)
        print("The age of the first person is : ",age)

P1 = Person("merna", 15)
print("############################################")
P2 = Person("Magdy",24)