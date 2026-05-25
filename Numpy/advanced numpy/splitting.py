"""
np.split()- normal i.e equal split
np.hsplit()- horizontal
np.vsplit()- vertical
"""
import numpy as np
arr1= np.array([40,50,60,80])
arr2 = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])


print(np.split(arr1, 4))
print(np.hsplit(arr1, 2))
print(np.vsplit(arr2, 3))