for i in range(2):
	print(i) # print 0 then 1

for i in range(4,6):
	print (i) # print 4 then 5
"""
Explanation:
If only single argument is passed to the range method, 
Python considers this argument as the end of the range and the default start value of range is 0. 
So, it will print all the numbers starting from 0 and before the supplied argument.
For the second for loop the starting value is explicitly supplied as 4 and ending is 5.
"""