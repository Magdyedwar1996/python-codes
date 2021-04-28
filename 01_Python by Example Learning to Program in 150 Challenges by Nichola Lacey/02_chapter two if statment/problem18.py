"""
Ask the user to enter a number. If it is under 10,
display the message “Too low”, if their number is
between 10 and 20, display “Correct”, otherwise
display “Too high”
"""
while True :
    number = int(input("Enter a number plz : "))
    if number < 10 :
        print("Too low!")
    elif number > 10 and number < 20 :
        print("Correct")
    else :
        print("Too high")