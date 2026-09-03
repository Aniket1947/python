import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr)

print(arr.reshape(3,3))
print(arr.shape)
arr1=arr[0:5]
print(arr1)

arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2[1][2])
print(arr2.shape)
flat=arr2.flatten()
print(flat)

arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr3)
print(arr3[:,0,2])