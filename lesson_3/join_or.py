"""
Problem
input: list, string delimiter, string last word
output: string

rules
explicit: 
- delimiter is only used when list has 3 or more elements
- last word is prepended when list has 2 or more elements
- default value of delimiter is ', '
- default value of last word is 'or'
implicit:
- empty list returns empty string

Data Structures
A new list may be necessary to join elements of passed in list using delimiter and last word

Algorithm
1. Create variable list_size and determine the length of the list
2. Create a shallow copy of list called list_copy
3. Itereate through list_copy and convert integers to strings
- if size is 0, return empty string
- if size is 1, return element at index 0
- if size is 2, return joined elements with last word
- if size is greater than 2
    - reference -1 index of list and prepend last word to element with a space in between
    - return joined elements with delimiter
"""

def join_or(lst, delimiter = ", ", prepend_word = "or"):
    new_lst = [str(el) for el in lst]
    
    match len(new_lst):
        case 0:
            return ""
        case 1:
            return new_lst[0]
        case 2:
            return f"{new_lst[0]} {prepend_word} {new_lst[1]}"
        
    new_lst[-1] = f"{prepend_word} {new_lst[-1]}"
    return delimiter.join(new_lst)


print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"