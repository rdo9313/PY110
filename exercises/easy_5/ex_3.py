def remove_vowels(strings):
    VOWELS = 'aeiou'
    result = []

    for string in strings:
        no_vowel = ''
        for char in string:
            if char.lower() not in VOWELS:
                no_vowel += char

        result.append(no_vowel)

    return result

# RegEx version
# import re

# def remove_vowels(strings):
#     return [re.sub(r'[aeiou]', '', string, flags = re.I) for string in strings]

# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True