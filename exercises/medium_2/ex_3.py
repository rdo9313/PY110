"""
P
Given three angles as arguments, return one of four strings describing a triangle type or invalid triangle

E
- 'right' => one angle is 90
- 'acute' => all three angles less than 90
- 'obtuse' => one angle greater than 90
- 'invalid' => sum of three angles is 180 and every angle must be greater than 0
- all input angles are integer values

D
input: three integers
output: string

A
- create a list with input angles
- if sum of list != 180 or list includes a 0, return 'invalid'
- if list includes a 90, return 'right'
- if one element in list is greater than 90, return 'obtuse'
- return 'acute'
"""

def triangle(angle1, angle2, angle3):
    angles = [angle1, angle2, angle3]

    if (0 in angles) or (sum(angles) != 180):
        return 'invalid'

    if 90 in angles:
        return 'right'

    for angle in angles:
        if angle > 90:
            return 'obtuse'

    return 'acute'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True