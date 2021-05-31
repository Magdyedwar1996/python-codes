a = True
b = False
c = False

if not a or b:
	print(1)
elif not a or not b and c:
	print(2)
elif not a or b or not b and a:
	print(3)
else:
	print(4)

# the answer will be 3




"""
Explanation : 
In Python the precedence order is first NOT then AND 
and in last OR. So the if condition and second elif condition 
evaluates to False while third elif condition is evaluated to be 
True resulting in 3 as output."""