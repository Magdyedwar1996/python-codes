check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']

check2 = check1
check3 = check1[:]

check2[0] = 'Code'
check3[1] = 'Mcq'

count = 0
for c in (check1, check2, check3):
    print(c)
    if c[0] == 'Code' :
        count += 1
    if c[1] == 'Mcq' :
        count += 10
print(count)


"""
Explanation:
When assigning check1 to check2, we create a second reference to the same list. 
Changes to check2 affects check1. 
# //////////////////////////////////////////////////////////////////////////
When assigning the slice of all elements in check1 to check3, 
we are creating a full copy of check1 which can be modified independently 
# ///////////////////////////////////////////////////////////////
(i.e, any change in check3 will not affect check1).
So, while checking check1 ‘Code’ gets matched and count increases to 1,
but Mcq doest gets matched since its available only in check3.
Now checking check2 here also ‘Code’ gets matched resulting in count value to 2.
Finally while checking check3 which is separate than both check1 
and check2 here only Mcq gets matched and count becomes 12.
"""