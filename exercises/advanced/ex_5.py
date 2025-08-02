"""
P
Given a list, use merge sort to sort the list.

E
- input can be a list of strings or numbers

D
input: list
output: list

A
- divide list in half into two sublists
- divide sublists in half into four
- repeat until each element is in its own list
- iterate through each sublist and merge nested pair
- repoeat until length of list is equal to initial list

1. if length of the sublist is 1, return sublist
2. get half index by length of input list // 2
3. pass recursively into merge_sort for both halves
4. return the merged list of first and second half
"""
def merge(lst1, lst2):
    lst1_copy = lst1[:]
    lst2_copy = lst2[:]
    result = []

    while lst1_copy and lst2_copy:
        if lst1_copy[0] > lst2_copy[0]:
            result.append(lst2_copy.pop(0))
        else:
            result.append(lst1_copy.pop(0))

    result += lst1_copy + lst2_copy
    return result

def merge_sort(lst):
    if len(lst) == 1:
        return lst

    first_half = merge_sort(lst[:len(lst) // 2])
    second_half = merge_sort(lst[len(lst) // 2:])

    return merge(first_half, second_half)

# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)

