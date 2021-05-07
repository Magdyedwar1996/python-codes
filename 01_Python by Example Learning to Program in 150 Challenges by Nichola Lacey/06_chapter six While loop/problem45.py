"""
045
Set the total to 0 to start with. While the total is 50 or less, ask
the user to input a number. Add that number to the total and
print the message “The total is… [total]”. Stop the loop when
the total is over 50
"""
total = 0
while total <= 50 :
    number = float (input("Enter a number : "))
    total = total + number

print(f"The total is {total}")