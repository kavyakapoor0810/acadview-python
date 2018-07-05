#numpy

import numpy as np
'''
a = np.array([1,2,3])
print(type(a))
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0,0],b[0,1],b[1,0])

# martices
a = np.zeros((2,2))
print(a)

b= np.ones((1,2))
print(b)

c = np.full((2,2),7)
print(c)

d = np.eye(2)
print(d)

e = np.random.random((2,2))
print(e)

import  numpy as np
a = np.arange(15).reshape(3,5)
print(a)

print(a.shape)

print(a.ndim)

print(a.dtype.name)

print(a.itemsize)

print(a.size)

a = np.array([[1,2,3],[4,5,6],[7.8,9],[10,11,12]])

print(a)

b =np.array([0,2,0,1])
print(a[np.arange(4),b])
a[np.arange(4),b]+=10
print(a)

a= np.array([[1,2],[3,4],[5,6]])
bool_idx=(a)
print(bool_idx)

'''


x=np.array([[1,2],[3,4]])
y=np.array([[5,6],[7,8]])

v= np.array([9,10])
w= np.array([11,12])
print (v.dot(w))

