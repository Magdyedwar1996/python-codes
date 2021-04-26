'''
Python Program to check Armstrong Number
n digits
abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....

'''
# way one to find the order of a num
num = int(input("enter the num :"))
def num_digits(num) :
    n = 0
    while num >= 1 :
        n = n + 1
        num = num / 10
    return  n

order = num_digits(num)
print("the  number of digits is :", order)
n = order

# to fine if the num id armstrong
def is_armestrong(num):
    for i in tuple(num) :
        output =(num[i]**n)
        temp = output
        output = 0
        total_output = total_output + temp
    return total_output

ut = is_armestrong(num)
if ut == num :
    print("the num is armestrong")
else :
    print("the num is not armestrong")







# way two to find the order of a num
'''num = int(input("enter the num :"))
def num_digits(num) :
    n = 1
    while num >= 10 :
        n = n + 1
        num = num / 10
    return  n
order = num_digits(num)
print("the  number of digits is :",order)'''

