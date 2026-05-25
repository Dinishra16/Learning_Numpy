import numpy as np
arr = np.array([[10,20,30],
                [40,50,60]])# number of rows and column should be same as if not, it wont be homogeneous
print(arr)
newarr= np.delete(arr, 0, axis = 0)
print(newarr)