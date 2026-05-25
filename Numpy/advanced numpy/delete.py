"""
np.delete(array, index, axis= none)- will return new array and old array will remain unchanged
"""
import numpy as np
arr = np.array([10,20,30,40,50,60,70,80])
print(arr)
newarr= np.delete(arr, 0)
print(newarr)