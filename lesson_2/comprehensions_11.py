dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

list_of_vowels = []
for lst in dict1.values():
    for word in lst:
        for char in word:
            if char in 'aeiou':
                list_of_vowels.append(char)

list_of_vowels = [char for lst in dict1.values() 
                  for word in lst 
                  for char in word if char in 'aeiou']

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']