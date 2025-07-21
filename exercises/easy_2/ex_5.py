def interleave(lst1, lst2):
    result = []
    
    for el in zip(lst1, lst2):
        result.extend(el)
    
    return result

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True