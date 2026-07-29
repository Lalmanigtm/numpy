# 1. <---------------- mathematical operation -------->
# import numpy as np 

# arr = np.array([1,2,3])

# print(arr + 5)
# print(arr * 5)
# print(arr ** 2)

# now after this above compare python loop vs numpy to student

# 2. <-------Aggregation functions ------->
# aggregation functions are used when large dataset like in amazon and we have to find average price, max, number of items , and many more ....

import numpy as np 

arr = np.array([1,2,3])

print(np.sum(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))