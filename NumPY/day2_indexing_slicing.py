import numpy as np

array1 = np.array([[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16]])

#array[start:end:step]
#Starts at 0 index , end in 1 index , with 1 step
print(array1[0:1:1])
print(array1[2:0:-1])

print(array1[2:,2:])