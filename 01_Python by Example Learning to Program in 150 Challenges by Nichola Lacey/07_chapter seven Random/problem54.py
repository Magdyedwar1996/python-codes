"""
054
Randomly choose either heads or tails (“h” or “t”). Ask
the user to make their choice. If their choice is the same
as the randomly selected value, display the message
“You win”, otherwise display “Bad luck”. At the end, tell
the user if the computer selected heads or tails.
"""
import random
heads_or_tails = ["h","t"]
while 1 :
    computer_choice = random.choice(heads_or_tails)
    user_choice = input("Choose either head or tail : ")
    if computer_choice == user_choice:
        print("You win ")
    else :
        print("Bad luck ")

    print("the computer chose ",computer_choice+"\n")