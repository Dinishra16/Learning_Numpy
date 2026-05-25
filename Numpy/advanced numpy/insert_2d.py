import numpy as np
arr = np.array([[10,20],
                [30,40],
                [50,60],
                [70,80]])
newarr= np.insert(arr, 2, [100,200],0)
newarrc= np.insert(arr, 2, 100,1)
newarrn= np.insert(arr, 2, [100,200],None) # flatten the array

print("row:",newarr)
print("column:")
print(newarrc)
print("flatten:",newarrn)