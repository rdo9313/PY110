"""
P
Replace an input string with all 'number words' converted to its corresponding digit character.

E
- input string contains no punctuation
- it is assumed that number words are case insensitive

D
input: string
output: string
intermediate: list containing number words

A
- initialize a list containing number words
- split input string by space and itereate over each word
- if word is in list, concat number word conversion to empty string, else concat word
- return new string

1. Initialize empty list 'result' and a list 'number_words' containing number words from 'zero' to 'nine'
2. Split input string by space and iterate over each word
3. check if lowercased word is in 'number_words'
    - if True, append str(index) of word to 'result'
    - if False, append word to 'result'
4. return 'result' joined by a space
"""

def word_to_digit(text):
    result = []
    number_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for word in text.split(' '):
        lowercased_word = word.lower()
        if lowercased_word in number_words:
            result.append(str(number_words.index(lowercased_word)))
        else:
            result.append(word)

    return ' '.join(result)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True