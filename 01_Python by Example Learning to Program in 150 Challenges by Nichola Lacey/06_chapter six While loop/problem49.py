"""
Create a variable called
compnum and set the value
to 50. Ask the user to enter a
number. While their guess
is not the same as the
compnum value, tell them if
their guess is too low or too
high and ask them to have
another guess. If they enter
the same value as
compnum, display the
message “Well done, you
took [count] attempts”.
"""
compnum = 50
count = 0
number = 0
while number != 50 :
    count+= 1
    number = int(input("Enter a number : "))
    if number == 50 :
        print(f"Well done, you took {count} attempts")
        break
    elif number > 50 :
        print("Your number is too high ")
    elif number < 50 :
        print("your number is too low ")



























