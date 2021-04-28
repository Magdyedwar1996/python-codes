"""
006
Ask how many slices
of pizza the user
started with and ask
how many slices
they have eaten.
Work out how many
slices they have left
and display the
answer in a user friendly format
"""
Started_Number = int(input("plz , Can you tell me how many slices of pozza you start with :"))
Eaten_Number = int(input("i'm sorry but plz tell me how many you have eaten : "))
Left_Number  = Started_Number - Eaten_Number
print("The left number of pizza is :",Left_Number)
