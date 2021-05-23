def isPhoneNumber(text):
    # checking the length of the characters of expression
    if len(text) != 12:
        return False

    # checking the first three characters if they are numbers
    # if any of them is not a number it will return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    # checking the four character if it is a hyphen
    if text[3] != '-':
        return False

    # checking the first three characters if they are numbers
    # if any of them is not a number it will return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    # checking the four character if it is a hyphen
    if text[7] != '-':
            return False

    # checking the first three characters if they are numbers
    # if any of them is not a number it will return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True

print("415-555-4242 is a phone number:")
print(isPhoneNumber('415-555-4242'))

print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))