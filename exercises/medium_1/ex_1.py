"""
P
Move the first element of a list to the end of the list, but do not modify the original list.

E
- if input is empty list, return empty list
- if input is not a list, return None
- the elements within input list can be of any type

D
input: any type
output: new list

A
- check if input is not a list, return None if True
- check if input is an empty list, return empty list if True
- slice input[1:] + input[:1]
"""

def rotate_list(lst):
    if not isinstance(lst, list):
        return None

    if lst == []:
        return []

    return lst[1:] + lst[:1]


# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])