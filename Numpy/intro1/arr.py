#multi-dimension array- matrix
import numpy as np
matrix= np.array([[2,4,6],
                  [8,10,12]])
print(matrix)
#2d - rows and column
#creating arrary with default value
#np.zeroes(shape) (3) 
zeroes_array = np.zeros(3)  #it means that we are filling all the elements of the array as 0
print(zeroes_array)

# now we wnat to fill the array with all elements as 1
#ones(shape)
ones_array= np.ones((2,3))
print(ones_array)

#full function- now we want to give a specific value to it 
#full(shape,value)
filled= np.full((2,2),7) #with full we get the element that we chose as here it is 7, as the matrix and (2,2) are number of rows and column
print(filled)

#creating sequence of number in numpy
#arrange(start,stop,step)
arrr= np.arange(1,10,2)
print(arrr)

#creating identity matrix
#eye(size)
iden= np.eye(4)
print(iden)