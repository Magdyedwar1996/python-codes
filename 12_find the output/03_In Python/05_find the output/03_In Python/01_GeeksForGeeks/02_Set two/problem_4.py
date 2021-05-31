counter = {}
def addToCounter(country):
	if country in counter:
		counter[country] = counter[country] + 1
	else:
		counter[country] = 1

addToCounter('China')
addToCounter('Japan')
addToCounter('china')
addToCounter('Japan')
addToCounter('China')
addToCounter('China')



print(len(counter))
print(counter)