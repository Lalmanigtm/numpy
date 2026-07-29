# Fancy Indexing = selecting multiple elements at once
# Boolean Masking
# think numpy as an excel sheet where you want to access the single sell we use indexing and when we want to excess the multiple rows and column we choose slicing.
# numpy follow zero based indexing.
"""
array[index]  for 1d array
array[row, column] for 2d or more d array
"""

# import numpy as np

# arr = np.array([1,2,3,4,5,6,7])

# print(arr[0])
# print(arr[3])
# print(arr[-2])
# print(arr[10])   # which is not happn so error appear in terminal

# <------slicing----------->
# Extracting subset of Data
# array[start:stop:step]   start = indexing number || stop = end = indexing number and excluded.  || step default value is 1

import numpy as np

arr = np.array([1,2,3,4,5,6,7])

print(arr[1:5]) # index 1 to 4
print(arr[:5]) # index 0 to 4
print(arr[1:5:2]) # index 1 to 4 with step 2
print(arr[::5]) # index 1 to 4
print(arr[::-1]) # index 1 to 4