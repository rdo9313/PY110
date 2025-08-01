"""
P
Given an integer argument, return a value that is a featured number that is greater than the input

E
- 'Featured number' => odd, multiple of 7, all digits occur exactly once
- return error msg if there is no next featured number
- largest possible featured number is 9876543201

D
input: integer
output: integer or error

A
- iterate from a range starting from input + 1 to largest possible featured number
- check if number is a featured number, return current number if True
- return error msg

1. Create 'largest_feature_num' and set to 9876543201.
2. Iterate from range(input + 1, largest_feature_num + 1)
3. Pass iteration as arg to 'is_featured_num' function
4. if True, return iteration value
5. return error msg

is_featured_num
1. initialize a empty list 'digits'
2. convert arg to a string and iterate over each char and append to 'digits'
3. return True if arg is odd, multipe of 7, and length of set of 'digits' is equal to length of 'digits'
"""

LARGEST_FEATURED_NUM = 9876543201
error = ("There is no possible number that "
         "fulfills those requirements.")

def is_featured_num(number):
    digits = [char for char in str(number)]

    return number % 2 == 1 and number % 7 == 0 and len(set(digits)) == len(digits)

def next_featured(number):
    for num in range(number + 1, LARGEST_FEATURED_NUM + 1):
        if is_featured_num(num):
            return num

    return error



print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True
print(next_featured(9876543201) == error)       # True