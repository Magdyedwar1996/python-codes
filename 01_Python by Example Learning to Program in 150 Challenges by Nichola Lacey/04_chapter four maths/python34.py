"""
034
Display the following message:
    1) Square
    2) Triangle
      If the user enters 1, then it should ask them for
the length of one of its sides and display the
area.
      If they select 2, it should ask for the base
and height of the triangle and display the area. If
they type in anything else, it should give them a
suitable error message.
"""
while 1 :
    print(" 1) Square\n 2) Triangle")
    Choice = int(input("choose 1 for Square  or 2 Triangle  : "))
    if Choice == 1:
        side = float(input("Enter the length of the side of the square : "))
        Area = side * side
        print("The are of the square is : ", Area)
        print("#"*50)
    elif Choice == 2 :
        base = float(input("Enter the base of the triangle : "))
        height = float(input("Enter the height of the triangle : "))
        Area = base * height
        print("The area of the trianle is : ",Area)
        print("#"*50)
    else :
        print("sorry , wrong choice , try again ")
        print("#"*50)
