"""
077
Change program 076 so that once the user has completed their list of names, display the
full list and ask them to type in one of the names on the list. Display the position of that
name in the list. Ask the user if they still want that person to come to the party. If they
answer “no”, delete that entry from the list and display the list again
"""
People = []
print("Enter the names of three people you want to invite  ")
for i in range(3):
    Input = input(f"Name {i+1}: ")
    People.append(Input)

count = 3
while True :
    Ans  = input("Do you want to add more people:  ")
    Ans = Ans.lower()
    if Ans =="no":
        break
    else :
        count += 1
        Input = input("Enter Name : ")
        People.append(Input)

print(People)
name = input("Enter one of these names : ")
Index = People.index(name)
print(Index)
ANS = input(f"Do you still want this {name} to come to the party :")
ANS = ANS.lower()
if ANS =="yes":
    pass
else:
    del People[Index]
print(People)
#print(count)