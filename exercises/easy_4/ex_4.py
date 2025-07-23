def order_by_value(dictionary):
    return sorted(dictionary.keys(), key = lambda key: dictionary[key])

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True