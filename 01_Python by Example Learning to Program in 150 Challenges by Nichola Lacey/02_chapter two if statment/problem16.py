"""
016
Ask the user if it is raining and convert their answer to lower case
so it doesn’t matter what case they type it in. If they answer “yes”,
ask if it is windy. If they answer “yes” to this second question,
display the answer “It is too windy for an umbrella”, otherwise
display the message “Take an umbrella”. If they did not answer yes
to the first question, display the answer “Enjoy your day”
"""

answer1 = input("Is it raining ? ")
answer1 = answer1.lower()
if answer1 =="yes":
    answer2 = input("Is it windy ? ")
    answer2 = answer2.lower()
    if answer2 =="yes":
        print("sorry , It is too windy for an umbrella")
    else:
        print("then you should take an umbrella")

else:
    print("You can enjoy your day")