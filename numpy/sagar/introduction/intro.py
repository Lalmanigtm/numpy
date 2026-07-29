# temperatures = [33.4, 33, 31.7, 29.9, 40]

# total = 0
# for temp in temperatures:
#     total += temp

# average = total/len(temperatures)
# print(average)  

# Then click run button and we will see the output in the terminal. so this python list is possible for only small data but fo data like ( 1 million, 10 millions, billions in above temperature data) using python can take a lots of time and memory so we prefer numpy.
# Who is the founder of numpy ?


# <---------- so prefer numpy ------------------>
# import numpy as np
# # instead of as np we are allow to write any like : import numpy as xxx    bu we have to use xxx.array(). np is a standard form. 

# temperatures = np.array([33.4, 33, 31.7, 29.9, 40,33.4, 33, 31.7, 29.9, 40,33.4, 33, 31.7, 29.9, 40,33.4, 33, 31.7, 29.9, 40,33.4, 33, 31.7, 29.9, 40,33.4, 33, 31.7, 29.9, 40])
# average = np.mean(temperatures)
# print(average)

# with this program we do not need loops, and is fast and less memory consumption.
# 50 to 100 times fast than python list in speed

# <----------- Concept of array----------->
# if you are a teacher and you have to write a marks:
# without array:
# marks1 = 85 
# marks2 = 95 
# marks3 = 80 
# marks4 = 50 
# marks5 = 75 

# BUT same with array:
# marks = [85,95,80,50,75]

# <------------ Method 1. Creating arrays from python lists ----------->
# we use this method when we already have a python list and have to convert into array
# python list:
# marks = [89, 93, 80, 99]

# convert this above python list to array as this : 
# array = np.array([element1, element 2, element 3,......])
# array_marks = np.array([89, 93, 80, 99])  # then we are success......

# <------------ Method 2. Creating arrays with default values ----------->
# we use this method when we do not have any elements and we have a duty to create a completely new arrays. eg : np.zeros(3) for 1d array, (2,3) or (3,2) for 2 d array

# import numpy as np

# zeros_array = np.zeros(4)
# zeros_second_array = np.zeros((3,2))
# ones_array = np.ones(3)
# ones_second_array = np.ones((1,3))
# print(zeros_array)
# print(zeros_second_array)
# print(ones_array)
# print(ones_second_array)


# create a full shape array: full(shape, value)
# import numpy as np

# full_array = np.full((2,3),6)
# print(full_array)

# <--------- Creating sequence of number in numpy------->
# arange(start,stop,step)

# import numpy as np
# array = np.arange(1,20, 3)
# print(array)

# <--------- Creating Identity matrix in numpy------->
# eye(size)

import numpy as np 

identity_matrix = np.eye(2)
print(identity_matrix)