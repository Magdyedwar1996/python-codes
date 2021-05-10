"""
056
Randomly pick a whole number between 1
and 10. Ask the user to enter a number and
keep entering numbers until they enter the
number that was randomly picked
"""
import random
computer_choice = random.choice(range(11))
user_choice = int(input("Choose a number between 1: 10 >> "))
if computer_choice==user_choice:
    print("correct choice ")
else:
    print("incorrect choice !")
    while computer_choice!= user_choice:
        user_choice = int(input("Choose a number again between 1: 10 >> "))
        if computer_choice == user_choice:
            print("correct choice ")
            break
        else :
            print("incorrect choice !")

print(f"the computer choice was {computer_choice}")