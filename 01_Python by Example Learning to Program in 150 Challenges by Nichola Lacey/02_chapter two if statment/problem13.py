"""
013
Ask the user to enter a
number that is under
20. If they enter a
number that is 20 or
more, display the
message “Too high”,
otherwise display
“Thank you”.
"""
while 1 :
    number = int(input("Enter a number less than 20 :"))
    if number < 20 :
        print("Thank you ")
    else:
        print("Too high!")