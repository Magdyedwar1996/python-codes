"""
046
Ask the user to enter
a number. Keep
asking until they enter
a value over 5 and
then display the
message “The last
number you entered
was a [number]” and
stop the program
"""
number = 0
while number < 5 :
    number = float(input("Enter a number : "))
print("The last number you entered was ", number)
