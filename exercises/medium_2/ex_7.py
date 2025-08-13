"""
P
Given a list, return the bubble sorted list

E
- the returned list should be the same list as the input (mutated)
- the input will contain at least two elements
- if passing through list without making any swaps, list is considered sorted

D
input: list
ouptut: list

A
- iterate through range from 0 to length of input list
- check if element at index is > element at index + 1
    - if True, swap elements
- repeat step 1 until no swaps are performed
- return mutated list

1. initialize 'swap' to False which determines whether a swap occured while iterating
2. iterate through index of range from 0 to length - 1 of input list
3. check if element at index > element at index + 1
    - if True, swap elements. set 'swap' to True
4. repeat iteration until 'swap' is False after end of iteration
"""

def bubble_sort(numbers):
    while True:
        swap = False
        for index in range(len(numbers) - 1):
            if numbers[index] > numbers[index + 1]:
                numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]
                swap = True

        if not swap:
            break

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True

