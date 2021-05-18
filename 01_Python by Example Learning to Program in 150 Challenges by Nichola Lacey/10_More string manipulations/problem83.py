"""
083
Ask the user to type in a word in upper case. If they
type it in lower case, ask them to try again. Keep
repeating this until they type in a message all in
uppercase
"""
Uper_Input = input("Enter a word all in upper case : ")
magdy = 0
while magdy == 0 :
    if (Uper_Input.isupper()):
        print("Thank You ")
        magdy = 1
    else :
        print("Try again \n ")
        Uper_Input = input("Enter a word all in upper case : ")

