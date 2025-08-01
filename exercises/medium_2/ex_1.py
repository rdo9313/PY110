"""
P
Take in a string and return a dictionary that shows the percentages of lowercase, uppercase, and neither characters

E
- string will always contain at least one character
- percentage must be rounded to two decimal points

D
input: string
output: dictionary
intermediate: list for lowercase, uppercase, and neither

A
- initialize an empty dictionary 'result'
- iterate through characters of input string
- check if character is alphabetical
    -if True, check if lowercase or uppercase and append to corresponding list
    -if False, append to neither list
- get percentages of the three lists by dividing the length of list by length of input string
- round the percentages to two decimals, convert to string, and update 'result'
- return 'result'

1. Initialize empty dictionary 'result', empty lists 'lowercase', 'uppercase', and 'neither'
2. Iterate through chars of string and check if char is alphabetical
    - if True, check if char is lowercase
        -if True, append char to 'lowercase'
        -if False, append char to 'uppercase'
    - if False, append char to 'neither'
3. Divide lengths of lists by length of input string and assign to 'lowercase_percentage', 'uppercase_percentage', and 'neither_percentage'
4. Round the percentages to two decimals, convert to string, and update 'result' with corresponding keys
5. return 'result' dictionary
"""

def letter_percentages(text):
    result = {}
    lowercase = 0
    uppercase = 0
    neither = 0
    text_length = len(text)

    for char in text:
        if char.islower():
            lowercase += 1
        elif char.isupper():
            uppercase += 1
        else:
            neither += 1

    lowercase_percentage = (lowercase / text_length) * 100
    uppercase_percentage = (uppercase / text_length) * 100
    neither_percentage = (neither / text_length) * 100

    result['lowercase'] = f"{lowercase_percentage:.2f}"
    result['uppercase'] = f"{uppercase_percentage:.2f}"
    result['neither'] = f"{neither_percentage:.2f}"

    return result



expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)