#1 Import the numpy package under the name np

import numpy as np

#2 Print the numpy version and the configuration.

print np.__version__
print np.__config__.show()

#3 Create a null vector of size 10

nullvec = np.zeros(10)
print nullvec

#4 Create a null vector of size 10 but the fifth value which is 1

Z= np.zeros(10)
Z[4]=1
print Z

#5 Create a vector with values ranging from 10 to 49

Z= np.arange(10,50)
print Z

#6 Create a 3x3 matrix with values ranging from 0 to 8

Z = np.arange(9).reshape((3,3))
print Z

#7 Find indices of non-zero elements from [1,2,0,0,4,0]
print np.nonzero([1,2,0,0,4,0])

#8 Create a 3x3 identity matrix

Z= np.eye(3)
print Z

#9 Create a 5x5 matrix with values 1,2,3,4 just below the diagonal

Z= np.diag([1,2,3,4],k=-1)
print Z

#10 Create a 3x3x3 array with random values
R = np.random.random((3,3,3))
print R


