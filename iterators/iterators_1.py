# define a list
my_list = [4, 7, 0, 3]
my_tuple = (4, 7, 0, 3)

# get an iterator using iter()
my_iter = iter(my_list)
print("its type is : ", type(my_iter))

my_tuple_iter = iter(my_tuple)
print("its type is : ", type(my_tuple_iter))

# iterate through it using next()

# Output: 4
print(next(my_iter))

# Output: 7
print(next(my_iter))

# next(obj) is same as obj.__next__()

# Output: 0
print(my_iter.__next__())

# Output: 3
print(my_iter.__next__())

# This will raise error, no items left
# next(my_iter)
