lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

def increment_value(dictionary):
    for key in dictionary:
        dictionary[key] += 1
    
    return dictionary

new_lst = [increment_value(el) for el in lst]

print(new_lst == [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}])