"""
055
Randomly choose a number between 1 and 5. Ask the user to pick a
number. If they guess correctly, display the message “Well done”,
otherwise tell them if they are too high or too low and ask them to pick a
second number. If they guess correctly on their second guess, display
“Correct”, otherwise display “You lose”
"""
import random
numbers= [1,2,3,4,5]
while 1 :
    computer_choice = random.choice(numbers)
    user_choice = int(input("Choose number from 1 : 5 . you have two choices : "))
    if computer_choice == user_choice:
        print("You win, Correct ")

##################################################################################
    elif computer_choice > user_choice:
        user_choice = int(input("""Sorry , it is not a correct number \n Your number is lower than the number chosen by the computer
 \nTry again please ,Choose number from 1 : 5 .\n You have only one choice remaining : """))
        if computer_choice == user_choice:
            print("You win, Correct ")
        else :
            print("You lose ")
##################################################################
    elif computer_choice < user_choice:
        user_choice = int(input("""Sorry , it is not a correct number \nYour number is higher than the number chosen by the computer
Try again please ,Choose number from 1 : 5 .\nYou have only one choice remaining : """))
        if computer_choice == user_choice:
            print("You win, Correct ")
        else:
            print("You lose ")
    print(f"the computer chose {computer_choice}"+"\n")