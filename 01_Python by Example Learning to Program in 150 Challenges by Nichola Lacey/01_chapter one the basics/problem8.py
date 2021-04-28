"""
008
Ask for the total price of the bill, then ask how
many diners there are. Divide the total bill by the
number of diners and show how much each
person must pay
"""

tatal_price = float(input("What is the total price of the bill :\n"))
Diners = int (input("How many diners are there : \n "))
Each_Diner = tatal_price / Diners
print("Each diner will pay :", Each_Diner)