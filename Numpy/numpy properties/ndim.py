#checks number of dimension- using when we need to know how many dimension 
import numpy as np
arr_1d= np.array([1,2,3])
arr_2d= np.array([[1,2,3],
                  [4,5,6]])
arr_3d= np.array([
              [[1,2],
               [5,6],
               [8,9]]])  #return number of dimension 
print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)