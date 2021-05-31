class A(object):
	val = 1
class B(A):
	pass
class C(A):
	pass
print(A.val, B.val, C.val)
B.val = 2
print (A.val, B.val, C.val)
A.val = 3
print (A.val, B.val, C.val)

"""
Explanation:
In Python,{{{{ class variables are internally handled as dictionaries}}}}. 
If a variable name is not found in the dictionary of the current class, 
the class hierarchy (i.e., its parent classes) are searched until the referenced 
variable name is found, if the variable is not found error is being thrown.
So, in the above program the first call to print() prints the initialized value i.e, 1.
In the second call since B. val is set to 2, the output is 1 2 1.
The last output 3 2 3 may be surprising. Instead of 3 3 3, here B.val
reflects 2 instead of 3 [[[[[since it is overridden earlier]]]]].
"""
