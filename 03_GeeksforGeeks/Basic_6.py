'''
# Python program to print all
# prime number in an interval
'''

start = int(input("enter the start num :"))
end   = int(input("enter the end num : "))

for val in range(start,end+1):
    if val > 1 :

        for n in range(2, val):
            out = val % n
            if (out) == 0 :
                break
        else:
            print(val)
"""
for val in  range(Start , End + 1 ) :
    for i in range( 2 , End):
        if (val % i) == 0:
            break
    else:
        print(val)
"""



