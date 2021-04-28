"""
017
Ask the user’s age. If they are 18 or over, display the
message “You can vote”, if they are aged 17, display the
message “You can learn to drive”, if they are 16, display
the message “You can buy a lottery ticket”, if they are
under 16, display the message “You can go Trickor-Treating”.
"""
while 1:
    age = float(input("Enter your age plz :"))
    if age >= 18 :
        print("You can vote")
    elif age == 17 :
        print("You can learn to drive ")
    elif age == 16 :
        print("You can buy a lottery ticket ")
    else :
        print("You can go Trickor-Treating")