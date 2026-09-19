

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print("1-dim",arr1,sep= "\n",end = '\n\n')


arr2 = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
print("1-dim",arr2,sep ='\n', end ='\n\n')


arr3 = np.array([[[1, 2],[5, 6]],[[9, 10],[11, 12]]])
print("multi-dim",arr3, sep ='\n')



zeros = np.zeros((2,3))
print(zeros)

ones = np.ones((3,4))
print(ones)

identity = np.identity((5))
print(identity)

full_array = np.full((5,3),"mouna")
print(full_array)

range_arr = np.arange(5,0,-1)
print(range_arr)

np.random.seed(40)
rand_arr = np.random.randint(100)
print(rand_arr)
rand_int = np.random.randint(30,60)
print(rand_int)
rand_int = np.random.randint(1, 6, 8)
print(rand_int)
rand_int = np.random.randint(1, 6, (4, 3))
print(rand_int)

rand_float = np.random.rand(10)
print(rand_float)
rand_float = np.random.rand()
print(rand_float)

lang = ['html','python','mysql','javascript','css']
rand_choice = np.random.choice(lang ,3)
print(rand_choice)

arr = np.array([[1, 2],[3, 4],[5, 6],[7, 8],[2, 1]])
print(arr.shape)
reshaped = arr.reshape(1,10)
print(reshaped)
flattened = arr.flatten()
print(flattened)
transposed = arr.T
print(transposed)

#ACCESS ELEMENTS USING INDEX / SLICING
arr = np.array([10, 20, 30, 40,50])
print(arr[0])
print(arr[3])
print(arr[1:3])
print(arr[-1])

import numpy as np
matrix = np.array([[10, 20, 30],[40, 50, 60],[70,80,90]])

print(matrix[0:3,0])
print(matrix[0:3,1])
print(matrix[0:2,0:2])

arr = np.array([10, 15, 30, 40,50])
print(arr +10)
print(arr *2)
print(arr**0.5)
print(arr%2 == 0)
print(arr[arr%2!=0])

a = np.array([1, 2, 3, 4, 5, 6])
print(np.min(arr))
print(np.cumsum(arr))#[1, 3, 6, 10,15,21]
print(np.cumprod(arr))

unique_val =np.unique(arr)
print(unique_val)
split_arr = np.split(np.array([1, 2, 3, 4, 5, 6]), 3)
print(split_arr)

arr =np.array([10,20,30])
view_arr = arr.view()
view_arr[0] = 200
print(arr,view_arr)

copy_arr = arr.copy()
copy_arr[0] = 700
print(arr,copy_arr)

#MATRIX MULTIPLICATION
A = np.array([[1, 2], [3, 4]])
B = np.array([[4, 6],[9, 8]])
print(np.dot(A,B))

print(np.linalg.det(A))

print(np.linalg.inv(A))

eigenvalues ,eigenvectors = np.linalg.eig(A)
print(eigenvalues)

print(eigenvectors)

C = np.array([5, 10])
solution = np.linalg.solve(A,C)
print(solution)