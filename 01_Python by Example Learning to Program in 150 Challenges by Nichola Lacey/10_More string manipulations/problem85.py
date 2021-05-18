"""
085
Ask the user to type in their name
and then tell them how many vowels
are in their name
"""
vowel_list = ["o","u","i","e","a"]
Input = input("Enter your name plase : ")
Input = Input.lower()
count = 0
for i in range(len(Input)):
    if Input[i] in vowel_list:
        count+=1

print(f"There are {count} vowel letters in your name !")