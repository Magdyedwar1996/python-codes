# Python Program to find sum of array
# way one

def _sum(arr , n):
    print(arr)
    print(n)
    return (sum(arr , n ))
arr = [12, 3, 4, 15 ,56 , 789]

n = len(arr)
print(n)
ans = _sum(arr, n)
print("Sum of the array is ",ans)



# way two
arr = [ 5 , 7 , 8 , 98 ,787 , 147 , 256 ]
n = len(arr)
addition = sum(arr , n)
print(addition)