import numpy as np 
print(np.__version__)
nums = list(range(1000000))
total = 0
for n in nums:
    total+=n
print(total)