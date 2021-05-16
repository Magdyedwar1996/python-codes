"""
081
Ask the user to type in their favourite school subject.
Display it with “-” after each letter, e.g. S-p-a-n-i-s-h-.
"""
Subject = input("Enter your favourite school subject : ")
for i in range(len(Subject)):
    print(Subject[i] , end="-")
