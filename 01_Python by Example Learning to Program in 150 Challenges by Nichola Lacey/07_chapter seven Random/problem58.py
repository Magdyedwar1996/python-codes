"""
058
Make a maths quiz that asks five questions by randomly
generating two whole numbers to make the question
(e.g. [num1] + [num2]). Ask the user to enter the
answer. If they get it right add a point to their score. At
the end of the quiz, tell them how many they got correct
out of five
"""
import random
numbers = range(10000)
iterator = 0
count = 0
while iterator <5:
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    correct_result = num1 + num2
    user_result= int(input(f"what is the result of {num1} + {num2} = "))
    if correct_result == user_result :
        print("Great your result is correct ")
        count += 1
    else:
        print("No , your result is not correct !")

    iterator += 1

print(f"you have answered {count} correct ")























