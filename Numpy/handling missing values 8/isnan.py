import numpy as np
arr= np.array([1, np.nan, 3, 4, np.nan])
print (np.isnan(arr))

# true = nan is present 
# false = a number or value is present 
# we cannot compare the nan values
print (np.nan== np.nan)#  not comparable
