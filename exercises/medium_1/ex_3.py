def rotate_rightmost_digits(num, count):
    if count == 1:
        return num

    num = str(num)

    first_part = num[:-count]
    part_to_rotate = num[-count:]
    rotated_part = part_to_rotate[1:] + part_to_rotate[0]

    return int(first_part + rotated_part)

def max_rotation(num):
    for count in range(len(str(num)), 1, -1):
        num = rotate_rightmost_digits(num, count)

    return num

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True