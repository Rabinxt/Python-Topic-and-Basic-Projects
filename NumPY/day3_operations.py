import numpy as np

array = np.array([1,2,3])
print(array + 1) #add
print(array - 1) #subtraction
print(array / 2) #Division
print(array * 2) #Multiplication
print(array ** 2) #Power


#To find square
print(np.sqrt(array))

array2 = np.array([1.33 , 3.55 , 6.55])
print(np.round(array2))

#inbuilt pi function
print(np.pi)

#Finding area of circle Directly
Radii = np.array([2 , 3, 4])
print(np.pi * Radii **2 )

#Element-Wise Arithmetics

array11 = np.array([1, 2, 3])
array12 = np.array([4, 5, 6])
print(array11 + array12)


scores = np.array([ 13, 1000, 200 , 300, 432 , 56])
print(scores == 1000)