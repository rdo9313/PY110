lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_lst = []
for el in lst:
    new_lst.append(sorted(el, key = str))

print(new_lst)

new_lst = [sorted(el, key = str) for el in lst]
print(new_lst)

# [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]