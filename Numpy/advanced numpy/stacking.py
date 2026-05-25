"""
vstack()- rowwise
hstack()- column wise

"""
import numpy as np
arr1 = np.array([10,20,30]) # make it hoogeneous
arr2=  np.array([ 40,50,60])
print(np.vstack((arr1,arr2))) #vertical stack
