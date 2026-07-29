"""   
np.insert(array, index, value, axis=None)
array = original array
index = to change which index
value = the new value which will finally inserted
axis = 0 means add row-wise data
axis = 1 means add column-wise data
 """

#  inserting in 2d_array

# import numpy as np

# arr = np.array([10,20,30,40,50])
# print(arr)

# new_arr = np.insert(arr, 1, 87)
# print(new_arr)

# # inserting in 2d_array

# import numpy as np

# arr_2d = np.array([[1,2],[3,4]])
# print(arr_2d)

# new_arr_2d = np.insert(arr_2d, 1, [5,6], axis=0)
# new2_arr_2d = np.insert(arr_2d, 1, [7,8], axis=1)
# new3_arr_2d = np.insert(arr_2d, 1, [9,0], axis=None)
# print(new_arr_2d)
# print(new2_arr_2d)
# print(new3_arr_2d)

# Append = adding any element in last of array
# import numpy as np

# arr = np.array([1,2])
# new_arr = np.append(arr, [50,70])

# print(new_arr)

# concatenate arrays

""" 
np.concatenate((array1, array2), axis = 1)

axis = 0 means vertical stacking
axis = 1 means horizontal stacking
"""
# import numpy as np

# arr_1 = np.array([1,2])
# arr_2 = np.array([3,4])

# new_arr = np.concatenate((arr_1, arr_2), axis = 0)
# print(new_arr)

# Removing elements from array
# for 1d array
"""  
np.delete(array, index, axis = None)   axis = None means flatten array
"""
# import numpy as np

# arr = np.array([1,2,3,4,5,6])
# print(arr)

# new_arr = np.delete(arr, 1, axis = None)
# new2_arr = np.delete(arr, 1, axis = 0)
# new_arr = np.delete(arr, 1, axis = 1)
# print(new_arr)
# print(new2_arr)
# print(new_arr)

# for 2d array
import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6]])

# new_arr_2d = np.delete(arr_2d, 1, axis = None)
new_arr_2d = np.delete(arr_2d, 1, axis = 1)

print(new_arr_2d)