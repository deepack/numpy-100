
import numpy as np

#11 Create a 8x8 matrix and fill it with a checkerboard pattern

C = np.zeros((8,8))

C[0:8:2,0:8:2] = 1
C[1:8:2,1:8:2] = 1

print C

#12 Create a 10x10 array with random values and find the minimum and maximum values

T = np.random.random((10,10))
print np.min(T),np.max(T)

#13 Create a checkerboard 8x8 matrix using the tile function

a=np.array([[1,0],[0,1]])
np.tile(a,(4,4))

#14 Normalize a 5x5 random matrix (between 0 and 1)

Z= np.random.random((5,5))
Zmax = np.max(Z)
Zmin = np.min(Z)

Z = Z- Zmin / (Zmax-Zmin)
print Z

#15 Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)

Z= np.ones((5,3))
Y = np.ones((3,2))

M = np.dot(Z,Y)
print M

#16 Create a 5x5 matrix with row values ranging from 0 to 4

Z= np.zeros((5,5))
Z+= np.arange(5)
print Z

#17 Create a vector of size 10 with values ranging from 0 to 1, both excluded

Z = np.linspace(0,1,11,endpoint=False)[1:]

print Z

#18 Create a random vector of size 10 and sort it

Z=np.random.random(10)
Z.sort()


#19 Consider two random array A anb B, check if they are equal.

A = np.random.random((10,10))
B = np.random.random((10,10))
print np.allclose(A,B)


#20 Create a random vector of size 30 and find the mean value

Z= np.random.random(30)
print np.mean(Z)
