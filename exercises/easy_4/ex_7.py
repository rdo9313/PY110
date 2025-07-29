def leading_substrings(text):
    return [text[:i] for i in range(1, len(text) + 1)]

def substrings(text):
    result = []
    for i in range(len(text)):
        result.extend(leading_substrings(text[i:]))

    return result

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True