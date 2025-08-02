"""
P
Given a matrix, return a new matrix with the rows and columns of each element transposed

E
- returns a new matrix (list of sublists)
- matrix is always 3x3

D
input: list
output: list

A
- create an new 3x3 matrix (3 sublists in a list) filled with None values for nine elements
- Iterate through range of length of outer list
    - Iterate through range of length of sublist
- Get the value. Swap the rows and columns for new matrix and store value
- return new matrix

1. initialize 'result' as 3x3 matrix with 3 None elements in each sublist
2. Iterate through row of input list
3. Iterate through column of input list
4. assign value at row and column of input list to the swapped row and column of 'result' matrix
5. return new matrix
"""

def transpose(matrix):
    MATRIX_SIZE = len(matrix)
    result = [[None, None, None] for _ in range(MATRIX_SIZE)]

    for row in range(MATRIX_SIZE):
        for column in range(MATRIX_SIZE):
            result[column][row] = matrix[row][column]

    return result


matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True