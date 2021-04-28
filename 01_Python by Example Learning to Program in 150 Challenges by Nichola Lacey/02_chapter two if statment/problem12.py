"""012
Ask for two numbers. If
the first one is larger
than the second, display
the second number first
and then the first
number, otherwise show
the first number first and
then the second"""

number_1 = int(input("Enter two number plz :"))
number_2 = int(input())
if number_1 > number_2 :
    print("the second number is "+str(number_2)+" and the fist number is "+str(number_1))
else:
    print("the first number is "+str(number_1)+" and the second number is "+str(number_2))


