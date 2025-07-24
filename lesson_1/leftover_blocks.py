"""
Problem
input: integer (number of available blocks)
ouptut: integer (leftover blocks after building tallest possible structure)

rules
explicit: 
- blocks are all of same height, width, and length (cubes)
- top layer is one block
- each block in upper layer must be supported by four blocks in lower layer
implicit:
layer 1 -> 1 block
layer 2 -> 4 blocks
layer 3 -> 9 blocks
- number of blocks in a layer = layer number * layer number

Data Structure
- We won't need a data structure for this problem. We can simply use a loop
to iterate from layer 0 to n while summing the required blocks.

Algorithm
1. Create a function that passes in a layer number and returns total blocks required
    a. create a total variable and iterate from range(layer_number + 1).
    b. add the squared value of layer_number to total variable.
    c. return the total variable
2. Iterate layer_number from 1 to n and pass into function, check whether available blocks is greater
than total blocks required
    - if available blocks is greater or equal, continue the loop
3. Calculate leftover blocks by subtracting function(n - 1) by available blocks input and return the value
"""

def calculate_total_blocks(layer_number):
    return sum([num**2 for num in range(layer_number + 1)])

def calculate_leftover_blocks(available_blocks):
    layer_number = 0

    while available_blocks >= calculate_total_blocks(layer_number):
        total_blocks = calculate_total_blocks(layer_number)
        layer_number += 1
    
    return available_blocks - total_blocks


print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True