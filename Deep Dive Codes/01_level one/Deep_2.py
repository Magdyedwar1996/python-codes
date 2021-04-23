# all operators in python
#1 arithmetic operators



# bitwise operators
x = 10 ; y = 20
print(x&y)
print(x|y)
print(~y)
print(x>>3)
print(y>>3)
print(x<<3)
print(y<<2)

xx = 'Geeks for Geeks'
print('Geeks'  in xx)
print('for' in xx)

y = {3 : 'a' , 4 : 'b'}
print('b' in y)
print(3 and 4  in y )



w , r = 10 , 20
max = w if w>r else r
print(max)

a, b = 40 , 70
print((b, a)[a < b])
print({True: a, False: b} [a < b])

print ("Both a and b are equal" if a == b else
       "a is greater than b"  if a > b else "b is greater than a")

print (all([True, True, True, True]))
print (any ([True, True, True, True]))
print (any ([True, False, False, False]))
print (any([False,True, False, False]))



q = 20
if q < 10 :
    b = 'q < 10 '
else:
    b = 'q > 10'
print(b)



yu = 1 , 2 , 3
print(yu)
print(type(yu))

print('hello')





















