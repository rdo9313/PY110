"""
Problem
input: list of strings
output: list of sorted strings based on highest number of adjacent consonants.

rules
explicit: 
- retain original order if same number of adjacent consonants
- space in between two consonants are still considered adjacent
implicit: 
- strings may have no adjacent consonants
- strings is in highest to lowest order
- case is irrelevant

Data Strucutres
A list will be used to return a sorted list.

Algorithm
1. Create a function max_adj_consonants that returns the highest number of adjacent consonants for a string
    a. create "vowels" string that includes all vowels
    b. remove all spaces
    c. create max_consonants, current_consonants variable and set to 0
    d. iterate over chars of string
        - if char is alphabetical but not a vowel, current_consonants += 1
        - if max_consonants < current_consonants, update max_consonants = current_consonants
        - otherwise set current_consonants to 0
    e. return max_consonants if it is greater than 1, otherwise return 0
2. Sort the list with reverse = True and key = max_adj_consonants and return it
"""

def max_consonants_length(text):
    text = text.replace(" ","")
    vowels = 'aeiou'
    max_length = 0
    current_length = 0

    for char in text:
        if char.isalpha() and char not in vowels:
            current_length += 1
            if max_length < current_length:
                max_length = current_length
        else:
            current_length = 0

    return max_length if max_length > 1 else 0

def sort_by_consonant_count(lst):
    lst.sort(key = max_consonants_length, reverse = True)
    return lst

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']