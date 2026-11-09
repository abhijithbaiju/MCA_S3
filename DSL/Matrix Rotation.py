import numpy as np
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Matrix: \n",A)

print("90 degree Rotation:\n",np.rot90(A))

print("180 degree Rotation:\n",np.rot90(A,2))

print("270 degree Rotation:\n",np.rot90(A,3))

print("360 degree Rotation:\n",np.rot90(A,4))