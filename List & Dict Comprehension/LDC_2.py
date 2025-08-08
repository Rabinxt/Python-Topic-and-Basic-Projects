#  Project 2: Matrix Transpose (Intermediate Level)
# 🎯 Objective:
# Use nested list comprehension to transpose a 2D matrix.
# 📂 Requirements:
# Input: A 2D list (matrix)
# Output: Transposed matrix (rows become columns)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# In simple term
# for i in range(len(matrix[0])):
#     for row in matrix:
#         print(row[i])

print(f"Original Matrix :")
for num in matrix :
    print(num)
for num in transpose :
    print(num)