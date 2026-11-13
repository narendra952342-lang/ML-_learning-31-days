import numpy as np
arr = np.arange(5,51,5)
print(arr)

print(type(arr))
print(arr.dtype)
print(arr.size)
print(arr.ndim)

arr1 = arr.reshape(2,5)
print(arr1)