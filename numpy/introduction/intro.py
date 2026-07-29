temperatures = [33.4, 33, 31.7, 29.9, 40]

total = 0
for temp in temperatures:
    total += temp

average = total/len(temperatures)
print(average)  

# Then click run button and we will see the output in the terminal. so this python list is possible for only small data but fo data like ( 1 million, 10 millions, billions in above temperature data) using python can take a lots of time and memory so we prefer numpy.
# Who is the founder of numpy ?


# <---------- so prefer numpy ------------------>
import numpy as np
# instead of as np we are allow to write any like : import numpy as xxx    bu we have to use xxx.array(). np is a standard form. 

temperatures = np.array([33.4, 33, 31.7, 29.9, 40,33.4, 33, 31.7, 29.9, 40,33.4, 33, 31.7, 29.9, 40,33.4, 33, 31.7, 29.9, 40,33.4, 33, 31.7, 29.9, 40,33.4, 33, 31.7, 29.9, 40])
average = np.mean(temperatures)
print(average)

# with this program we do not need loops, and is fast and less memory consumption.
# 50 to 100 times fast than python list in speed

# <----------- Concept of array----------->
# if you are a teacher and you have to write a marks:
# without array:
marks1 = 85 
marks2 = 95 
marks3 = 80 
marks4 = 50 
marks5 = 75 

# BUTsame with array:
marks = [85,95,80,50,75]