# Python Program for array rotation
def array_rotate(arr , n ):
    for i in range(0 , n):
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp
    return  arr

arr = [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ]
n = len(arr)
arr_after_rotation = array_rotate(arr , n )
print(arr_after_rotation)