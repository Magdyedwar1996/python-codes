"""
059
Display five colours and ask the user to pick one. If they
pick the same as the program has chosen, say “Well
done”, otherwise display a witty answer which involves
the correct colour, e.g. “I bet you are GREEN with envy”
or “You are probably feeling BLUE right now”. Ask
them to guess again; if they have still not got it right,
keep giving them the same clue and ask the user to
enter a colour until they guess it correctly.
"""

import random
colours = ["orange", "Green", "BLUE", "black","white"]
computer_choice = random.choice(colours)
while 1 :
    user_choice = input("Choose a colour >> ")
    if computer_choice == user_choice:
        print("correct choice ")
        break

        #############################################
    elif computer_choice != user_choice:
        print("incorrect choice !\n  ")
        if computer_choice=="orange":
            print("I wish your T-shirt was orange , Try again ")

        elif computer_choice=="Green":
            print("I bet you are GREEN with envy , Try again ")

        elif computer_choice == "BLUE":
            print("You are probably feeling BLUE right now , Try again ")

        elif computer_choice =="white":
            print("I hope your life will be like this colour , Try again ")

        elif computer_choice == "black":
            print("I think this colour is pessimistic , Try again ")




#print(f"the computer choice was {computer_choice}")