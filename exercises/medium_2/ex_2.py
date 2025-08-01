"""
P
Using the input lengths of three sides of a triangle, return one of four strings that describe a triangle or is invalid.

E
- 'equilateral' -> all three sides are equal
- 'isosceles' -> two sides are equal while third is not
- 'scalene' -> all three sides have different lengths
- 'invalid' -> two shorter sides is <= longest side or any side has 0 length

D
input: three integers or floats
output: string
intermediate: list to sort the side lengths

A
- create a list for the input lengths and sort it
- if all lengths are equal, return equialteral
- if list includes 0 or sum of first two elements are not greater than last, return invalid
- if two elements are equal, return isosceles
- else return scalene

1. Initialize 'lengths' list with all input values, then sort it
2. Check if set of 'lengths' is equal to length 1
    - if True, return 'equilateral'
3. Check if list includes 0 or sum of first two elements is <= last element
    - if True, return 'invalid'
4. Check if set of 'lengths' is equal to length 2
    - if True, return 'isosceles'
5. return 'scalene'
"""

def triangle(num1, num2, num3):
    lengths = sorted([num1, num2, num3])

    if (0 in lengths) or (lengths[0] + lengths[1] <= lengths[2]):
        return 'invalid'

    if len(set(lengths)) == 1:
        return 'equilateral'

    if len(set(lengths)) == 2:
        return 'isosceles'

    return 'scalene'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True