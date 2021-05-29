# takes the value , then multiply it with 2, finally return the result to r
r = lambda q: q * 2
# takes the value , then multiply it with 3 ,finally return the result to s
s = lambda q: q * 3
# displaying the type of r
# print(type(r))

x = 2
# print("The type of x : ",type(x))
x = r(x)        # x  =  2 * 2

x = s(x)        # x = 4 * 3

x = r(x)        # x = 12 * 2

print (x)       # will print 24

# print("The type of x : ",type(x))
