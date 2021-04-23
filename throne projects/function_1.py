def myFun(x):
    x[0] = 20
    x[2] = 54
    print("x[4] = ", x[4])
    print("list[4] = ", list[4])
    print(x)
list = [10, 11, 12, 13, 14, 15]
myFun(list)
print(list)
print("list[4] = " ,list[4])