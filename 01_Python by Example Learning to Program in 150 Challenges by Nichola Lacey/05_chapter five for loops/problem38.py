"""
038
Change program
037 to also ask for a
number. Display
their name (one
letter at a time on
each line) and
repeat this for the
number of times
they entered.
"""
i = "0"
number = int(input("Enter a number : "))
name = input("Enter your name please : ")
name = list(name)
for i in range(number):
    for i in list(name):
       print(i)
    print("#"*20 + "\n")