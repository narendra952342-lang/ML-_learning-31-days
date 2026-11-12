import numpy as np
import time
nums = list(range(1000000))
arr = np.arange(1000000)
t0 = time.time()
sum(nums)
print("list :",time.time()-t0)
t0 = time.time()
arr.sum()
print("numpy :",time.time()-t0)