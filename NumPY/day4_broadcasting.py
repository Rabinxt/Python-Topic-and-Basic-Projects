import numpy as np

array1 = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,1,2,3],
                   [4,5,6,7]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print(array1 * array2)

#creating multiplacation table from 1 to 10
numbers1 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
numbers2 = np.array([[1,2,3,4,5,6,7,8,9,10]])
print(numbers2 * numbers1)