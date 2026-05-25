# np.isinf(array) - calculation that exceed python numbers , se we use it
import numpy as np
arr = np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(arr))
clean = np.nan_to_num(arr,posinf=  100, neginf= 200)
print(clean)