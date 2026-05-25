" slice[start:stop:step] ; start to end-1"

import numpy as np
arr = np.array([10,20,30,40,50,60,70,80,90,100])
print(arr[1:5]) #index 1 to 4
print(arr[:4]) #index 0 to 3
print(arr[::4]) 
print(arr[::-1])