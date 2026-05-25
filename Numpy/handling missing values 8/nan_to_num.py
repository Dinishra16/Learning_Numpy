# many models do not process nan so we use np.num_to_nan so we can exchange values 
import numpy as np
arr= np.array([1, np.nan, 3, 4, np.nan])
clean= np.nan_to_num(arr,nan= 100) # nan= 100 means that the value that is needed to be inserted will be 100 but the default value is 0
print (clean)
