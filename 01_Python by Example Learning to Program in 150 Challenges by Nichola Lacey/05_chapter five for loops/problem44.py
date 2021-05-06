"""
044
Ask how many people the user wants to invite to a party. If they enter a number below
10, ask for the names and after each name display “[name] has been invited”. If they
enter a number which is 10 or higher, display the message “Too many people”.
"""
number_of_people = int(input("Enter the number of people you want to invite : "))
if number_of_people < 10 :
    for i in range(number_of_people):
        name = input(f"Enter the name of the  invited number{i} :")
        print(f"[{name}] has been invited")
elif number_of_people>= 10 :
    print("Too many people ")

