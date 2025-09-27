import numpy as np

#for 1d array
oned_array = np.array([2,4,3,4,5,6,7,2,3,4,5,2,3,1,3])
print("Sorted 1 D array is: ", np.sort(oned_array))

#for 2d array 
twod_array = np.array([[3,4],
                       [5,6],
                       [4,1]])
#for sorting in column
print("Sorted 2D array in column is: ", np.sort(twod_array, axis=0))
#for sorting in rows
print("Sorted 2D array in rows: ", np.sort(twod_array, axis=1))


#Filtering

numbers = np.array([1,2,3,4,5,6,7,8,9,0])
even_numbers = numbers[numbers%2 == 0]
print(even_numbers)
odd_numbers = numbers[numbers % 2 != 0]
print(odd_numbers)

#Filtering with mask
mask = numbers > 5
print(numbers[mask])