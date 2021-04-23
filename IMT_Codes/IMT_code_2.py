Number = input("Please Enter The Number :")
Number = int(Number)

Result = 1
i = Number

while i > 0:
    Result = Result * i
    i = i - 1

print("Factorial of " + str(Number) + " = " + str(Result))