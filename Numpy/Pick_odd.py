import numpy as np

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
NdArray = np.arange(1,26).reshape(5,5)
print(NdArray)
# Afterwards use Boolean indexing to pick out only the odd numbers in the array
X_odd = NdArray[NdArray % 2 != 0 ]
print(X_odd)
