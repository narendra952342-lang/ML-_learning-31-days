import numpy as np
arr = np.arange(0,10,2)
print(arr)

# indexing
print(arr[0],arr[1])
print(arr[-1],arr[-4])

#slicing
print(arr[:])
print(arr[::])
print(arr[2:4])
print(arr[2:4:])
print(arr[2::2])
print(arr[:5:2])
print(arr[::2])

arr1 = np.array([
    [10,20,30,40],
    [2,4,5,6]])

#indexing
print(arr1[0,0])
print(arr1[0][0])

#slicing
print(arr1[:,2])
print(arr1[1,:])