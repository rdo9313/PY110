# def multiply_items(list_a, list_b):
#     return [list_a[idx] * list_b[idx] for idx in range(len(list_a))]

def multiply_items(list_a, list_b):
    return [num1 * num2 for num1, num2 in zip(list_a, list_b)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True