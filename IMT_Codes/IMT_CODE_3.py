height = input("please enter height : ")
height = int(height)

row = 0
while row < height:
    NumofSpace = height - row - 1
    NumofStar = (2 * row) + 1
    string = ""
    i = 0
    while i < NumofSpace:
        string = string + " "
        i = i + 1
    i = 0
    while i < NumofStar:
        string = string + "*"
        i = i + 1

    print(string)
    row = row + 1

row = height - 2
while row >= 0:
    NumofSpace = height - row - 1
    NumofStar = (2 * row) + 1
    string = ""
    i = 0
    while i < NumofSpace:
        string = string + " "
        i = i + 1
    i = 0
    while i < NumofStar:
        string = string + "*"
        i = i + 1

    print(string)
    row = row - 1