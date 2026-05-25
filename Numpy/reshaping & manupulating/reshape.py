# #reshaping - modify the dimension of array without changing data
# reshanpe(rows,column) specify new shape if dimension match
import numpy as np
arr = np.array([10,20,30,40,50,60,70,80,90,100])
rarr= arr.reshape(2,5)
print(rarr) 
