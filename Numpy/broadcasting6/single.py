# RULE OF BROADCASTING -
# 1- MATCHING DIMENSION-> THE DIMENSION OR SIZE SHOULD BE staticmethod
# 2- EXPANDING SINGLE ELEMENTS - [1,2,3]+10=[1+10,2+10,3+10]

# 3-  IN COMPATIBLE SHAPE - will throw error if the araay dimension is not same i.e shape is different 
#                            [1,2,3]+[1,2]=error


import numpy as np
prices = np.array([100,200,300,400,500,600,700,800,900,1000])
discount = prices*10/100

print(discount)
