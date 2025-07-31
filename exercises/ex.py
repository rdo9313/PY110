"""
P
Return a list of integers that represent how many letters each string in a input list occupy the positions that they would occupy in the alphabet

E
- Input lists only consist of alphabetic characters with no spaces
- Characters are case insensitive

D
input: list of strings
output: list of integers
Intermediary: string of lowercased alphabet

A
- Iterate over each character in each string of input list
- If the character exists in the alphabet string and the indices
of the character in string and alphabet match, increment a total
- After iterating through last character, push total to a new list
- Return list

1. Initialize 'alphabet' as a string of alpahbet characters.
2. Initialize 'result' as empty list.
3. Iterate through input list. Initialize 'match' to 0.
Iterate through chars of enumerated string.
4. If char in 'alphabet', check if current index and index of
char in 'alphabet' are equal.
    - Increment 'match' by 1 if True
5. At the end of each string iteration, append 'match' to 'result'
6. return 'result'
"""

def solve(lst):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []

    for string in lst:
        match = 0
        for idx, char in enumerate(string.lower()):
            if char in alphabet:
                if idx == alphabet.index(char):
                    match += 1
        result.append(match)

    return result

print(solve(['encode', 'abc', 'xyzD', 'ABmD']) == [1, 3, 1, 3])
print(solve(['abode', 'ABc', 'xyzD']) == [4, 3, 1])
print(solve(['abide', 'ABc', 'xyz']) == [4, 3, 0])
