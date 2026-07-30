# # apply 10% discount in every price
"""
 prices = [100,150,200,250,300]
 discount = 10  # 10%

 final_prices = []

 for price in prices:
     final_price = price - (price * discount/100)
     final_prices.append(final_price)

 print(final_prices)    
"""
# Broadcasting is a powerful mechanism in NumPy that allows arithmetic operations between arrays of different shapes. Broadcasting is a numpy way where we can perform operations in different arrays without using loops.
"""
 import numpy as np

 prices = [100,150,200,250,300]
 discount = 10  # 10%

 final_prices = prices - (prices * discount/100)
 print(final_prices) 
"""

# <----------How numpy handle arrays of different different shapes------------>
# 3 rules of Broadcasting:
#   1. Matching dimensions: [1,2,3] + [4,5,6] = [5,7,9]
#   2. Expanding single elements : [1,2,3] + 10  = [11,12,13]
#   3. incompatible shapes : if shapes do not meatch then we got error  : [1,2,3] +[1,2] = error
"""
import numpy as np

arr = np.array([100,200,300])
result = arr * 3
print(result)
"""
# from 1d to 2d
"""
import numpy as np

matrix = np.array([[1,2,3],[4,5,6]])  # 2x3 matrix
vector = np.array([7,8,9])

result = matrix + vector
print(result)

"""

# Getting error:
import numpy as np

arr1 = np.array([[1,2,3],[4,5,6]])  # 2x3 matrix
arr2 = np.array([7,8])  # shape(2,)

# result = arr2 + arr1
print(arr2 + arr1)
# output : ValueError: operands could not be broadcast together with shapes (2,) (2,3) 
