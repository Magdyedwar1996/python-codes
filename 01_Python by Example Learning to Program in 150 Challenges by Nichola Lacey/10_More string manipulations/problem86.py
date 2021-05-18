"""
086
Ask the user to enter a new password. Ask
them to enter it again. If the two passwords
match, display “Thank you”. If the letters are
correct but in the wrong case, display the
message “They must be in the same case”,
otherwise display the message “Incorrect”
"""

magdy = 1
while magdy == 1:
    user_password1 = input("Enter the password please : ")
    user_password2 = input("Confirm the password again please : ")
    if user_password1 == user_password2:
        print("Thank you ")
        magdy = 0
    elif user_password1.lower() == user_password2.lower():
        print("the letters are correct but in the wrong case \nThey must be in the same case")
    else :
        print("Incorrect")