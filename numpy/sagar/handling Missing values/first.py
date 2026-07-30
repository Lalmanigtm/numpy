# np.isnan(array)
"""
import numpy as np 

arr = np.array([1,2,np.nan,4,np.nan,6])

print(np.isnan(arr))

print(np.nan == np.nan)
"""
# Replace nan to number :
"""
# np.nan_to_num(array, nan=value)  [if not nan value then by default 0]
import numpy as np 

arr = np.array([1,2,np.nan,4,np.nan,6])

# cleaned_array = np.nan_to_num(arr, nan = 199)
cleaned_array = np.nan_to_num(arr)
print(cleaned_array)

"""
# for infinity values: np.isinf(arr) like: 1/0, 1000 ** 10000
import numpy as np 

arr = np.array([1,2,np.inf,4,-np.inf,6])

print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf=-1000)
print(cleaned_arr)



