"""
076
Ask the user to enter the names of three people they want to
invite to a party and store them in a list.
After they have entered all three names, ask them if they want to add another.
If they do, allow them to add more names until they answer “no”. When
they answer “no”, display how many people they have invited to
the party.
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
print(count)