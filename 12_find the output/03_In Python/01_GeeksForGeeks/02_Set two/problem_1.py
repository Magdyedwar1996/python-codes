class Acc:

    def __init__(self, id ):
        self.id = id
        # id = 666

    mm = 555
"""print(self.id)
        print(id)  
"""
# Instantiation of the class “Acc” does two things :
# 1- calls the method __init__
# passes the object as the self parameter.
acc = Acc(111)
print(acc.id)
print(acc.mm)
print(Acc.mm)

"""
Explanation: 
Instantiation of the class “Acc” automatically calls 
the method __init__ and passes the object as the self parameter. 
111 is assigned to data attribute of the object called id.
The value “555” is not retained in the object as it is not 
assigned to a data attribute of the class/object. So, 
the output of the program is “111”
"""