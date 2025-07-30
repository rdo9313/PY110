def unique_sequence(numbers):
    current = None
    result = []

    for num in numbers:
        if num != current:
            current = num
            result.append(current)

    return result

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True