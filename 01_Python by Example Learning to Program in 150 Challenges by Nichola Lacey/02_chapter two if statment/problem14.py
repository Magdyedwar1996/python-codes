"""
014
Ask the user to enter a
number between 10 and 20
(inclusive). If they enter a
number within this range,
display the message “Thank
you”, otherwise display the
message “Incorrect
answer”.
"""
while 1 :
    number = int(input("Enter a  number that is  [20 > number > 10] :  "))
    if (number <=20 and number >=10) :
        print("Thank you !")
    else:
        print("Incorrect answer")