import numpy as np 
arr = np.array([45,82,67,91,38,74,59,88])
marks = arr>=60
print(marks)
print(arr[arr>=60].mean())
mid = arr[(arr>=60)&(arr<85)]
print(mid)