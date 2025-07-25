lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_list = []
for element in lst:
    new_list.append(sorted(element))

print(new_list)

new_list = [sorted(element) for element in lst]
print(new_list)

# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]