import numpy
#creating array and finding dimension, shape, and printing my name from array
array1 = numpy.array(
    [
        [['A','B','C'],['D','E','F'],['G','H','I']],
        [['J','K','L'],['M','N','O'],['P','Q','R']],
        [['S','T','U'],['V','W','X'],['Y','Z','']],
    ]
)
print(array1.ndim)
print(array1.shape)
word = array1[1,2,2] + array1[0,0,0] + array1[0,0,1] + array1[0,2,2] + array1[1,1,1]
print(word)

#creating 3*3 array all element of 0
array2 = numpy.zeros((3,3))
print(array2)

#creating 3*3 array with all element of 1
array3 = numpy.ones((3,3))
print(array3)

#Some more array creating methods
numpy.full((2, 2), 7) # 2x2 array filled with 7
numpy.eye(3)          # 3x3 Identity matrix
numpy.arange(0, 10, 2) # [0 2 4 6 8]
numpy.linspace(0, 1, 5) # 5 numbers between 0 and 1
