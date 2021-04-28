"""
015
Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I don’t like [colour], I prefer red”.
"""
while 1 :
    colour = input("Enter your favourite colour : ")
    colour = colour.lower()
    if colour == "red":
        print("I like red too")
    else:
        print("I don't like  "+colour+" I prefer red !")