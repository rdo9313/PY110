def union(numbers1, numbers2):
    return set(numbers1 + numbers2)

print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True