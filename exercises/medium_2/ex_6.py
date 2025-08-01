"""
P
Given an integer, find the difference between the square of the sum of first count integers
and the sum of the square of first count integers.

E
- range starts from 1 and count should be included in range

D
input: integer
output: integer

A
- iterate through a range from 1 to count + 1
- find the total sum of all integers and square the sum
- find the square of each integer and sum together
- subtract step 2 - step 3
- return result

1. Initialize 'total_sum' and 'squared_sum' variables to 0
2. Iterate through range from 1 to input + 1
3. add iteration to total_sum
4. add squared iteration to squared_sum
5. square the value of 'total_sum' and subtract 'squared_sum' from it
6. return the difference
"""

def sum_square_difference(number):
    total_sum = sum(range(1, number + 1))
    squared_sum = sum(num**2 for num in range(1, number + 1))

    return total_sum**2 - squared_sum

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True