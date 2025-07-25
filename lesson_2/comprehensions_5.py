lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_odds(numbers):
    return sum([num for num in numbers if num % 2 == 1])

new_lst = sorted(lst, key = sum_odds)

print(new_lst == [[1, 8, 3], [1, 6, 7], [1, 5, 3]])