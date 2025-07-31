"""
P
Rotate the last 'count' digits of a number by moving the first digit of the number to the end.

E
- When 'count' is 1, return number as is
- count value is always greater than 0

D
input: two integers
output: integer
Intermediate: string type of number for slicing

A
- if 'count' is 1, return number as is
- Turn 'count' into negative value for indexing
- convert number into string
- concatenate string[:-count], string[-count + 1:], and string[-count]
- return concatenated string as integer
"""

def rotate_rightmost_digits(num, count):
    if count == 1:
        return num

    num = str(num)

    first_part = num[:-count]
    part_to_rotate = num[-count:]
    rotated_part = part_to_rotate[1:] + part_to_rotate[0]

    return int(first_part + rotated_part)

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True