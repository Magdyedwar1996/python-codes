# Python3 program to find maximum
# in arr[] of size n
def is_max(arr , n ):
    max = arr[0]
    for i in range( 1 , n ):
        if arr[i] > max :
            max = arr[i]
    return max

arr = [ 12 , 45 , 56 , 85 , 89 , 856 , 985 , 79, 32 , 145 , 659 ]
n = len(arr)
num = is_max(arr , n)
print("the max num is : ", num)
