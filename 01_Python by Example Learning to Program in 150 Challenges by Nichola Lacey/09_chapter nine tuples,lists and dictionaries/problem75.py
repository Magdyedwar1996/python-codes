"""
075
Create a list of four three-digit numbers. Display the list to the user, showing each item from
the list on a separate line. Ask the user to enter a three-digit number. If the number they
have typed in matches one in the list, display the position of that number in the list,
otherwise display the message  “That is not in the list"
"""
# this is the list
My_List = [145 , 789 ,654 ,369 ]
# printing the list each item in a separate line
for i in range(4):
    print(My_List[i])
# Asking the user to input a three digit number
Number = int(input("Enter a three_digit number please : "))
# Checking if the Entered number is aready existing or not
for j in range(4):
    if Number == My_List[j]:
        print( j )
        break
    elif j == 3 :
        print("That is not in the list")
