"""
021
Ask the user to enter their first name and then ask them to
enter their surname. Join them together with a space between
and display the name and the length of whole name.
"""
name = input("Enter your name please :")
surname = input("Enter your surname : ")
length = len(name) + len(surname)

print(f"{name} {surname} and their length is {length}")