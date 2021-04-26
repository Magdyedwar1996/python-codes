#Python Program for factorial of a number
# way one
n = int(input("enter your num : "))
def factorial(n):
    return 1 if (n==1 or n==0 ) else n*factorial(n-1)
fact = factorial(n)
print("the factorial of %d is : %d"%( n , fact ))




##way two
while True :
    num =input("enter the number you want to get its factorial : ")
    num = int(num)
    def factorial(num) :
         if (num < 0) :
            return 0
         elif( num == 1 or num == 0 ):
            return 1
         else :
            fact = 1
            while (num > 1) :
                fact = (num * fact)
                num = (num - 1)
            return fact

    gr = factorial(num)
    print("the factorial is : ",gr)


