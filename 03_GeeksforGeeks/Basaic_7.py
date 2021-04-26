# Python program to check if
# given number is prime or not
num = int(input("enter the num : "))
for n in range(2 , num//2):
    if (num % n )== 0 :
        print("the num you entered is not a  prime num .")
        break
else:
    print("the num you entered is a prime num ." )
