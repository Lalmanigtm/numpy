# Vectorization with python:
"""
list1 = [1,2,3]
list2 = [4,5,6]

result = [x+y for x,y in zip(list1, list2)]
print(result)
"""
# but in large dataset it takes a lots of time so now we do with fast vactorization means numpy method:

"""
import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

result = arr1 + arr2
print(result)
# in this if we add millions od data it will not be slow as python loop.result

"""
# another example:
import numpy as np

arr1 = np.array([1,2,3])
multipled = arr1 * 3

print(multipled)

"""
# Broadcasting VS Vectorization:
Broadcasting: it expand smaller array to large array to match .|| faster than loop. || eg: 1d ==> 2d .
Vectorization: apply entire array at once.  ||  100X faster than loop. || eg: matrix operations.
"""