import numpy as np

# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third
# column full of 3s, etc..
ones = np.ones((4,4))
broadcast = np.arange(1,5).reshape(1,4)
# Do not change the name of this array.
# Please don't print anything from your code! The TEST RUN button below will print your array.
X = ones * broadcast
print(X)