"""np.insert(array, index, value, axix= none)
array= original array
index- index value
valuse- value to be inserted 
axis - 0 for rows
     - 1 for column

"""
import numpy as np
arr = np.array([10,20,30,40,50,60,70,80])
newarr= np.insert(arr, 2, 100, 0)
print(newarr)