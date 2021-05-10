"""
057
Update program 056 so that it tells the
user if they are too high or too low before they
pick again.
"""

import random
computer_choice = random.choice(range(11))
while 1 :
    user_choice = int(input("Choose a number between 1: 10 >> "))
    if computer_choice==user_choice:
        print("correct choice ")
        break

        #############################################
    elif computer_choice < user_choice:
        print("incorrect choice !\nyour number is higher than the correct number !\n  ")

        ############################################################
    elif computer_choice > user_choice :
        print("incorrect choice !\nyour number is lower than the correct number !\n")


print(f"the computer choice was {computer_choice}")