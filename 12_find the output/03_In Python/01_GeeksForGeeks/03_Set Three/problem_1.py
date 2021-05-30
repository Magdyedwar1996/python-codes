class Geeks:
	def __init__(self, id):
		self.id = id
manager = Geeks(10230)

manager.__dict__['life']  =  49
manager.__dict__["maged"] = 1000

print("This is the [life member variable] : ",manager.life)
print("This is the [id member variable] : " ,manager.id)

# calculating the length of the dictionary of the object manager
print(len(manager.__dict__))
print(manager.life + len(manager.__dict__))


print(manager.maged)
print(len(manager.__dict__))
print(manager.maged + len(manager.__dict__))
print(manager.__dict__)

"""
In the above program we are creating a [member variable] having name ‘life’ 
by adding it directly to the [dictionary of the object ‘manager’] of class ‘Geeks’.
//////////////////////////////////////////////////////////////////////////////////////////
[Total number of items in the dictionary is 2], the variables ‘life’ and ‘id’.
Therefore the size or the length of the dictionary is 2 and the variable ‘life’
is assigned a value ’49’. So the sum of the variable ‘life’ and the size of the 
dictionary is 49 + 2 = 51.
"""