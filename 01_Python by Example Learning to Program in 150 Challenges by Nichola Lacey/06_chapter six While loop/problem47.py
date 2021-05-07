"""
047
Ask the user to enter a
number and then enter
another number. Add these
two numbers together and
then ask if they want to add
another number. If they
enter “y", ask them to enter
another number and keep
adding numbers until they
do not answer “y”. Once the
loop has stopped, display
the total.
"""
num1 = float(input("Enter a number : "))
num2 = float(input("Enter a number : "))
sum = num1 + num2
ans = 'y'
while ans == 'y':
    ans = input("Do you want to add another number. if yes enter \'y\': ")
    if ans !='y':
        break
    num = float(input("Enter a number : "))
    sum = sum + num

print("The total is : ", sum)
