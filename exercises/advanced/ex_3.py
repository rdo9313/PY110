"""
P
Given a matrix, return a new matrix rotated by 90 degrees

E
- input matrix is MxN
matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]
[0, 0] => [0, 1]  [1, 0] => [0, 0]
[0, 1] => [1, 1]  [1, 1] => [1, 0]
[0, 2] => [2, 1]  [1, 2] => [2, 0]
[0, 3] => [3, 1]  [1, 3] => [3, 0]

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

[0, 0] => [0, 2]  [1, 0] => [0, 1]  [2, 0] => [0, 0]
[0, 1] => [1, 2]  [1, 1] => [1, 1]  [2, 1] => [1, 0]
[0, 2] => [2, 2]  [1, 2] => [2, 1]  [2, 2] => [2, 0]

D
input: list
output: list

A
- Create a new list with the number of empty sublists equal to the length of the first sublist of input list
- iterate through range of length of first sublist
    - iterate through range of length of list - 1 to 0
- append value to new list indexed at first iteration
- return new list

1. initialize a new list with # of sublists equal to length of first sublist of input list as 'rotated_list'
2. iterate through range of length of input list - 1 to 0
    - iterate through range of 0 to length of first sublist
3. append value at input to new list indexed at element iteration
4. return new list
"""

def rotate90(matrix):
    rotated_list = [[] for _ in range(len(matrix[0]))]

    for sublist_idx in range(len(matrix) - 1, -1, -1):
        for element_idx in range(len(matrix[0])):
            rotated_list[element_idx].append(matrix[sublist_idx][element_idx])

    return rotated_list


matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
# new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
# print(new_matrix3 == matrix2)