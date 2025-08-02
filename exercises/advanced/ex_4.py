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

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)