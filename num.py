import numpy as np

# Generate random data
data = np.random.randn(2,3)
print(data)
print()

# The arrays are homogenous
data = data * 10
print(data)
print()

data = data + data
print(data)
print()

# Get the size of each dimesion
print(data.shape)
print()

# Get the array data type
print(data.dtype)
print()

# It's possible to create narray from Python sequences
data1 = [2,3,4,5,6,7]
arr1 = np.array(data1)
print(arr1)
print(arr1.shape)
print()

data2 =[[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
print(arr2)
# Get the array dimensions 
print(arr2.ndim)
print(arr2.dtype) # This dtype is an object
# What is a metadata? Data that contains information about other data
print(arr2.shape)
print()

# Creating arrays of 1s and 0s and specifing its shape
arr3 = np.ones((1,4,5))
print(arr3)
print()

arr4 = np.zeros((3,7,8))
print(arr4)
print()

arr5 = np.empty((2,2))
print(arr5)
print()

# Similar to range from Python
arr6 = np.arange(23)
print(arr6)
print()

# Fill an array with values that you provide
arr7 = np.full((2,3),5.9)
print(arr7)
print()

arr8 = np.eye(3)
print(arr8)
print()

arr9 = np.identity(5)
print(arr9)
print()

arr10 = np.array([1,2,3],dtype=np.float64)
arr11 = np.array([4,5,6],dtype=np.int32)
print(arr10)
print()
print(arr11)
print(arr11.dtype)
print()

# How to converto array types

arr12 = np.array([1,2,3,4,5])
print(arr12)
print(arr12.dtype)
print()

# astype always creates a new array
arr12 = arr12.astype(np.float64)
print(arr12)
print(arr12.dtype)
print()

# These operations don't modify the original array
arr13 = np.array([[1.,2.,3.], [4.,5.,6.]])
print(arr13)
print(arr13 * arr13)
print(arr13 + arr13)
print(arr13 - arr13)
print()

print(1/arr13)
print()
print(arr13 ** 2)

arr14 = np.array([[2.,4.,7.],[10.,21.,45.]])
print(arr13 < arr14)

arr15 = np.arange(10)
print(arr15[3])
print(arr15[3:9])
arr15[3:9] = 23
print(arr15)

arr_slice = arr15[3:9]
arr_slice[4] = 76
print(arr15)
# Apply the change to all the array
arr15[:] = 65
print(arr15)

# I have to explicitly copy values to copy an array
copy_arr = arr15[3:5].copy()

arr17 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr17[1])

old_values = arr17[0].copy()
arr17[0] = 34
print(arr17)
arr17[0] = old_values
print(arr17)
print()

arr16 = np.array([[1,2,3],[5,6,4],[5,6,7]])
print(arr16[2,1])

print(arr16[1:,:1])
print(arr16[:2, 2])
print()
print(arr16[2:, :])

names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
data = np.random.randn(7, 4)
print()
print(names)
print(data)
print()
print(names == 'Bob')

print()
print(data[names == 'Bob'])
 # print(data[np.array([True, False, False, True])])
print()

print(data[names != 'Bob'])
print()
# ~ means not
print(data[~(names == 'Bob')])
print()

mask = (names == 'Bob') | (names == 'Will')
print(mask)
print()

print(data[mask])
print()

data[data < 0] = 0
print(data < 0)
print(data)
print()

data[names != 'Joe'] = 7
print(data)

arr17 = np.empty((8,4))
for i in range(8):
    arr17[i] = i

print(arr17[[2,6,7]])
print()

arr18 = np.arange(32).reshape((8,4))
print(arr18)


print("\n",arr18[[0,1,2,3],[0,3,1,2]])

arr19 = np.arange(15).reshape((3,5))
print("\n",arr19)
print("\n",arr19.T)

arr20 = np.random.randn(6, 3)
print("\n",arr20)
print("\n",arr20.T)
print("\n",np.dot(arr20, arr20.T))

arr21 = np.arange(16).reshape((2,2,4))
print("\n",arr21)
print("\n\n",arr21.transpose((1,0,2)))

arr22 = np.arange(4).reshape((2,2))
print("\n",arr22)
print("\n",arr22.swapaxes(0,1))

arr23 = np.arange(10)
print("\n",np.sqrt(arr23))
print("\n",np.exp(arr23))
print(arr23)

x = np.random.randn(8)
y = np.random.randn(8)

print("\n",x)
print(y)
print(np.maximum(y,x))
