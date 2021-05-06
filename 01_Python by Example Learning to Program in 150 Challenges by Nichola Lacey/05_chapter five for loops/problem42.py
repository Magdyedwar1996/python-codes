"""
042
Set a variable called total to 0. Ask the user to enter
five numbers and after each input ask them if they
want that number included. If they do, then add the
number to the total. If they do not want it included,
don’t add it to the total. After they have entered all five
numbers, display the total.
"""
total = 0
i = 0
while i < 5 :
    num = float(input(f"Enter number{i} : "))
    with_or_not = input("Do you want this number included or not : ")
    with_or_not = with_or_not.lower()
    if with_or_not =="yes" :
        total = total + num
    elif with_or_not =="no":
        total = total + 0
    i +=1
print("The total is : ", total)

