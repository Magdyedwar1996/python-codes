#!/usr/bin/env python
# coding: utf-8

# In[4]:


from numpy import *
a = sin(30 * pi / 180 )
b = sin(deg2rad(30))
print(b)
print(a)


# In[37]:


import random
suits = ['hearts', 'clubs', 'spades', 'diamonds']
ranks = [int(r) for r in range(2, 13)]
magdy = list('AKQJ')
ranks.extend(magdy)
########################
suit = random.choice(suits)
rank = random.choice(ranks)
card = f'{rank} of {suit}'


# In[22]:


ranks


# In[23]:


magdy


# In[24]:


suits


# In[32]:


suit


# In[35]:


rank


# In[45]:


card


# In[43]:


card


# In[44]:


card


# In[6]:


from  numpy import *

a = mod(20,7)
b = power(2,5)
print(a)
print(b)


# In[7]:


a = [[1,2,3],[5,3,6],[9,6,5]]
b = array(a)
print(a)
print(b)


# In[8]:


c = type(a)
d = type(b)
c


# In[9]:


d


# In[12]:



sd = array([range(i, i + 3) for i in [2, 4, 6]])

print(sd)


# In[19]:


import pandas as pd 

dic_movie = { 
    "movie":["Avengers: Endgame", "Avatar", "Titanic", "Star Wars: The Force Awakens", "Avengers: Infinity War"], 
    "collections":[2.796, 2.789, 2.187, 2.068, 2.048],
    "release_yr":[2019, 2009, 1997, 2015, 2018]}

movie_df = pd.DataFrame(dic_movie)
movie_df


# In[32]:


import numpy as np
a = np.arange(30).reshape(2,3,5)
print(a)


# In[33]:


a.shape


# In[34]:


a.ndim


# In[38]:


type(a.dtype)


# In[39]:


a.size


# In[40]:


a.itemsize


# In[43]:


c = np.array([[1, 2], [3, 4]], dtype=complex)
c


# In[45]:


from numpy import pi
x = np.linspace(0, 2 * pi, 4)        # useful to evaluate function at lots of points
f = np.sin(x)
f


# In[46]:


print(np.arange(10000).reshape(100, 100))


# In[3]:


import numpy as np 
import time 


# In[4]:


x = np.random.random(1000000)
print(x)
print(len(x))


# In[5]:


start = time.time()
print(start)


# In[6]:


start = time.time()
sum(x) / len(x)
print(time.time()- start)


# In[7]:


start = time.time()
sum(x) / len(x)    # this to get tha mean by the usaul way 
print(time.time()- start)


# In[8]:


start = time.time()
np.mean(x)   # this is to get the mean by the numpy mean function 
print(time.time()- start)


# In[9]:


x = np.random.random(1000000)
np.save("my_array",x)


# In[11]:


magdy = np.load("my_array.npy")
magdy
merna = magdy
print(magdy)
print(merna)


# In[6]:


import numpy as np
x = np.array([1, 2, 3.0,"magdy", 4, 5])
print('x = ', x)
print(type(x))
print(x.dtype)
print(x.ndim)


# In[14]:


# 2-D array
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
Y.ndim
print(Y)


# In[17]:


y = np.zeros((2, 3, 4))
print(y)
y.ndim


# In[10]:


# We create a 1D ndarray that contains only integers
x = np.array([[1.0, 2, 3, 4, 5],[6,7,8,9,10]])

# We print information about x
print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)


# In[14]:


# We create a rank 1 ndarray that only contains strings
x = np.array(['Hello', 'World', 'Merna','Magdy'])

# We print information about x
print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)


# In[15]:


# We create a rank 1 ndarray from a Python list that contains integers and strings
x = np.array([1, 2, 'World'])

# We print information about x
print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)


# In[16]:


# We create a rank 1 ndarray of floats but set the dtype to int64
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)

# We print the dtype x
print('x = ', x)
print('The elements in x are of type:', x.dtype)


# In[17]:


# We create a rank 1 ndarray
x = np.array([1, 2, 3, 4, 5])

# We save x into the current directory as 
np.save('my_array', x)


# In[19]:


y = np.load("my_array.npy")
y


# In[21]:


import numpy as np

# create numpy array of letters a-j
letter_array = np.array(["a",'b','c','d','e','f','g','h','i','j'])
print("Letter Array: ", letter_array)

# get dtype of array
print("dtype of array: ", letter_array.dtype)

# get shape of array
print("shape of array: ", letter_array.shape)


# get size of array
print("size of array: ", letter_array.size)


# In[24]:


# We create a 3 x 4 ndarray full of zeros. 
X = np.zeros((3,4))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)


# In[29]:


# We create a 3 x 2 ndarray full of ones. 
X = np.ones((3,2),dtype = int)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype) 


# In[30]:


# We create a 2 x 3 ndarray full of fives. 
X = np.full((2,3), 5) 

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)  


# In[34]:


# We create a 5 x 5 Identity matrix. 
X = np.eye(5,dtype = int)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)  


# In[35]:


# Create a 4 x 4 diagonal matrix that contains the numbers 10,20,30, and 50
# on its main diagonal
X = np.diag([10,20,30,50])

# We print X
print()
print('X = \n', X)
print()


# In[37]:


# We create a rank 1 ndarray that has sequential integers from 0 to 9
x = np.arange(10)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 


# In[38]:


# We create a rank 1 ndarray that has sequential integers from 4 to 9. 
x = np.arange(4,10)

# We print the ndarray
print()
print('x = ', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 


# In[44]:


# We create a rank 1 ndarray that has 10 integers evenly spaced between 0 and 25.
x = np.linspace(0,25,10,endpoint = False,dtype = int)

# We print the ndarray
print()
print('x = \n', x)
print()

# We print information about the ndarray
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 


# In[45]:


# We create a rank 1 ndarray with sequential integers from 0 to 19
x = np.arange(20)

# We print x
print()
print('Original x = ', x)
print()

# We reshape x into a 4 x 5 ndarray 
x = np.reshape(x, (4,5))

# We print the reshaped x
print()
print('Reshaped x = \n', x)
print()

# We print information about the reshaped x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype) 


# In[47]:


# We create a rank 1 ndarray with 10 integers evenly spaced between 0 and 50,
# with 50 excluded. We then reshape it to a 5 x 2 ndarray
X = np.linspace(0,50,10).reshape(5,2)

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)


# In[48]:


# We create a 3 x 3 ndarray with random floats in the half-open interval [0.0, 1.0).
X = np.random.random((3,3))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in x are of type:', X.dtype)


# In[52]:


import numpy as np

# Using the Built-in functions you learned about on the
# previous page, create a 4 x 4 ndarray that only
# contains consecutive even numbers from 2 to 32 (inclusive)

X = np.linspace(2,32,16).reshape(4,4)
print(X)


# In[53]:


# We create a rank 1 ndarray that contains integers from 1 to 5
x = np.array([1, 2, 3, 4, 5])

# We print x
print()
print('x = ', x)
print()

# Let's access some elements with positive indices
print('This is First Element in x:', x[0]) 
print('This is Second Element in x:', x[1])
print('This is Fifth (Last) Element in x:', x[4])
print()

# Let's access the same elements with negative indices
print('This is First Element in x:', x[-5])
print('This is Second Element in x:', x[-4])
print('This is Fifth (Last) Element in x:', x[-1])


# In[54]:


# We create a rank 1 ndarray that contains integers from 1 to 5
x = np.array([1, 2, 3, 4, 5])

# We print the original x
print()
print('Original:\n x = ', x)
print()

# We change the fourth element in x from 4 to 20
x[3] = 20

# We print x after it was modified 
print('Modified:\n x = ', x)


# In[55]:


# We create a 3 x 3 rank 2 ndarray that contains integers from 1 to 9
X = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print X
print()
print('X = \n', X)
print()

# Let's access some elements in X
print('This is (0,0) Element in X:', X[0,0])
print('This is (0,1) Element in X:', X[0,1])
print('This is (2,2) Element in X:', X[2,2])


# In[56]:


# We create a 3 x 3 rank 2 ndarray that contains integers from 1 to 9
X = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print the original x
print()
print('Original:\n X = \n', X)
print()

# We change the (0,0) element in X from 1 to 20
X[0,0] = 20


# We print X after it was modified 
print('Modified:\n X = \n', X)


# In[58]:


# We create a rank 1 ndarray 
x = np.array([1, 2, 3, 4, 5])

# We print x
print()
print('Original x = ', x)

# We delete the first and last element of x
x = np.delete(x, [0,4])

# We print x with the first and last element deleted
print()
print('Modified x = ', x)


# We create a rank 2 ndarray
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We print Y
print()
print('Original Y = \n', Y)

# We delete the first row of y
w = np.delete(Y, 0, axis=0)

# We delete the first and last column of y
v = np.delete(Y, [0,2], axis=1)

# We print w
print()
print('w = \n', w)

# We print v
print()
print('v = \n', v)


# In[4]:


# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)

# We print X
print()
print('X = \n', X)
print()

# We select all the elements that are in the 2nd through 4th rows and in the 3rd to 5th columns
Z = X[1:4,2:5]

# We print Z
print('Z = \n', Z)

# We can select the same elements as above using method 2
W = X[1:,2:5]

# We print W
print()
print('W = \n', W)

# We select all the elements that are in the 1st through 3rd rows and in the 3rd to 4th columns
Y = X[:3,2:5]

# We print Y
print()
print('Y = \n', Y)

# We select all the elements in the 3rd row
v = X[2,:]

# We print v
print()
print('v = ', v)

# We select all the elements in the 3rd column
q = X[:,2]

# We print q
print()
print('q = ', q)

# We select all the elements in the 3rd column but return a rank 2 ndarray
R = X[:,2:3]

# We print R
print()
print('R = \n', R)


# In[3]:


import numpy as np
# We create a 4 x 5 ndarray that contains integers from 0 to 19
X = np.arange(20).reshape(4, 5)
# We print X
print()
print('X = \n', X)
print()


# In[5]:


# We select all the elements that are in the 2nd through 4th rows and in the 3rd to 5th columns
Z = X[1:4,2:5]

# We print Z
print('Z = \n', Z)


# In[6]:


# We can select the same elements as above using method 2
W = X[1:,2:5]

# We print W
print()
print('W = \n', W)


# In[7]:



# We select all the elements that are in the 1st through 3rd rows and in the 3rd to 4th columns
Y = X[:3,2:5]

# We print Y
print()
print('Y = \n', Y)


# In[8]:


# We select all the elements in the 3rd row
v = X[2,:]

# We print v
print()
print('v = ', v)


# In[9]:


# We select all the elements in the 3rd column
q = X[:,2]

# We print q
print()
print('q = ', q)


# In[10]:


# We select all the elements in the 3rd column but return a rank 2 ndarray
R = X[:,2:3]

# We print R
print()
print('R = \n', R)


# In[16]:


import numpy as np
# Let's create a rank 2 ndarray
X = np.random.randint(1,20000, size=(200,5))
print("Shape of X is: ", X.shape)
print(X)


# In[21]:


# Create a rank 1 ndarray that contains a randomly chosen 10 values between `0` to `len(X)` (50)
# The row_indices would represent the indices of rows of X
row_indices = np.random.randint(0,50, size=(10,3))
print("Random 10 indices are: \n", row_indices)


# In[23]:


# Create 3 x 3 ndarray with repeated values
X = np.array([[1,2,4],[5,2,8],[1,2,3]])

# We print X
print()
print('X = \n', X)
print()

# We print the unique elements of X 
print('The unique elements in X are:',np.unique(X))


# In[24]:


# We create a 5 x 5 ndarray that contains integers from 0 to 24
X = np.arange(25).reshape(5, 5)

# We print X
print()
print('Original X = \n', X)
print()


# In[25]:


# We use Boolean indexing to select elements in X:
print('The elements in X that are greater than 10:', X[X > 10])
print('The elements in X that less than or equal to 7:', X[X <= 7])
print('The elements in X that are between 10 and 17:', X[(X > 10) & (X < 17)])


# In[26]:


X[(X > 10) & (X < 17)] = -1


# In[27]:


X


# In[31]:


X[(X < 10) | (X > 17)] = 0


# In[32]:


X


# In[ ]:


# We create a rank 1 ndarray
x = np.array([1,2,3,4,5])

# We create a rank 1 ndarray
y = np.array([6,7,2,8,4])

# We print x
print()
print('x = ', x)

# We print y
print()
print('y = ', y)

# We use set operations to compare x and y:
print()
print('The elements that are both in x and y:', np.intersect1d(x,y))
print('The elements that are in x that are not in y:', np.setdiff1d(x,y))
print('All the elements of x and y:',np.union1d(x,y)

