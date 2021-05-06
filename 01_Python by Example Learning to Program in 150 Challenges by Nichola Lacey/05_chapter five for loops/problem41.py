"""
Ask the user to enter their
name and a number. If the
number is less than 10, then
display their name that
number of times; otherwise
display the message “Too
high” three times.
"""
while 1 :
    i = 0
    name = input("Enter your name please :")
    number = int(input("Enter a number : "))
    if number < 10 :
        for i in range(number):
            print(name)
        print("#"*50 + "\n" + "@"*50)
    elif number >= 10 :
        while i < 3 :
            print("Too high ")
            i += 1
        print("#"*50 + "\n" + "@"*50)


