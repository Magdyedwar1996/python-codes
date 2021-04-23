print("Please Enter Ten Values :")

OldNumber = 0
Sum = 0
i = 0
while i < 10:
    Number = input()
    Number = int(Number)
    if (Number > OldNumber):
        Max = Number
    if (Number < OldNumber):
        Min = Number

    OldNumber = Number
    Sum = Sum + Number
    i = i + 1

Avg = Sum / 10
print("Avg= ", Avg)
print("Max= ", Max)
print("Min= ", Min)