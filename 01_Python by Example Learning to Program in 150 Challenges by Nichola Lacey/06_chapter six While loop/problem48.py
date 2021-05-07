"""
048
Ask for the name of somebody the user wants to invite
to a party. After this, display the message “[name] has
now been invited” and add 1 to the count. Then ask if
they want to invite somebody else. Keep repeating this
until they no longer want to invite anyone else to the
party and then display how many people they have
"""
people = input("Enter the name of the person you want to invite : ")
print(f"{people} has been invited ")
count = 1
ans = 'yes'
while ans =="yes":
    ans = input("Do you want to invite another people : ")
    ans = ans.lower()
    if ans !="yes":
        break
    people = input("Enter the name of the person you want to invite : ")
    print(f"{people} has been invited ")
    count +=1

print("The total number of people invited  is : ", count)
