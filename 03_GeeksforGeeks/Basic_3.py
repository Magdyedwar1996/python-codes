'''
Python Program for simple interest
Simple interest formula is given by:
Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate
'''
P = int(input("enter the principle amount : "))
T = int(input("enter the time : "))
R = int(input("enter the rate : "))
SI = (P*T*R)/100
print("the simple interest is :",SI)
