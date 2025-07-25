"""
Problem
input: list that contains dictionaries
output: list that contains dictionaries with only even numbers

data structure
list with dictionaries

algorithm
1. iterate through each dictionary within the list
2. pass dict.values() into a function even_num_only that checks if all numbers are even
    a. iterate through lists of dict.values()
    b. iterate through numbers of each list
    c. if a number is odd, return False
    d. return True
3. if the function returns True, append current dictionary to new_list
4. return the list
"""

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def even_num_only(collection):
    for list in collection:
        for number in list:
            if number % 2 == 1:
                return False

    return True       

new_lst = [subdict for subdict in lst if even_num_only(subdict.values())]


print(new_lst == [{'e': [8], 'f': [6, 10]}])