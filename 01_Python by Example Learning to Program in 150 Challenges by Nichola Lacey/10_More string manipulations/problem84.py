"""
Ask the user to type in their postcode.
Display the first two letters in uppercase.
"""
Postcode = input("Enter your postcode please : ")
Upper = Postcode[0:2]
print(Upper.upper())