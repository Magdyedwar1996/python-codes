"""
050
Ask the user to enter a number between
10 and 20. If they enter a value under 10,
display the message “Too low” and ask
them to try again. If they enter a value
above 20, display the message “Too high”
and ask them to try again. Keep repeating
this until they enter a value that is
between 10 and 20 and then display the
message “Thank you”.
"""
while 1:
    number = int(input("Enter a number between 10 and 20 :"))
    if number>10 and number<20:
        print("Thank you ")
        break
    elif number < 10 :
        print("too low , try again ")
    elif number > 20:
         print("Too high , try again")
    else:
        print("You entered a wrong number ")