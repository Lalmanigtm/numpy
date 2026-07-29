# Re-shaping & Manipulating Data = 
# Reshaping = Change the shape of array(Dimension) without modify the data. like change 1D array ==> 2D array OR 2D array ==> 3D array  without modifying the data.

#  """ 
#  array.reshape(rows, columns) specify new shape if dimensions match  """ 

# import numpy as np

# arr = np.array([1,2,3,4,5,6,7,8])

# reshaped_arr = arr.reshape(2,4)

# print(reshaped_arr)
# Reshaping does not create a copy but only change a view.

# <-----------Flattening Array---------->
# convert the multi dimensional array into 1D array.
"""
.ravel() -> view
.flatten() -> copy
"""

import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6]])

print(arr_2d.ravel())
print(arr_2d.flatten())