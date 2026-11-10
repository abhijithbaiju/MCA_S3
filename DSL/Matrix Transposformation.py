import numpy as np


A = np.array([[1, 2],
              [3, 4]])

print("Original Matrix:")
print(A)

print("\nTranspose of Matrix:")
print(A.T)


print("\nInverse of Matrix:")
print(np.linalg.inv(A))


print("\nDeterminant of Matrix:")
print(np.linalg.det(A))


B = np.array([1, 2, 3, 4, 5, 6])

print("\nOriginal Array:")
print(B)

print("\nReshaped Matrix:")
print(B.reshape(2, 3))
