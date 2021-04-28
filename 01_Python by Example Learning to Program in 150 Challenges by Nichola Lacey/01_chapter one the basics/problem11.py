"""
011
ask the user to enter a number over 100 and then enter a number under
10 and tell them how many times the smaller number goes into the larger
number in a user-friendly format.
"""

larger_Number = int (input("Enter a number over than 100 : "))
smaller_Number = int(input("Enter a number less than 10 : "))
Number_Of_Times = larger_Number // smaller_Number
print(str(Number_Of_Times) + " times")