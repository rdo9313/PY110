"""
P
Find the fibonacci index by number of digits specified by argument

E
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

D
input: integer
output: integer

A
- while loop that breaks when number of digits of fib num is equal to argument
- iterate from 1, convert fib num type to string and check length
- if length is equal to argument, return current iteration value
"""
import sys

sys.set_int_max_str_digits(50_000)

memo = {}
def fibonacci(num):
    if num in (1, 2):
        return 1
    elif num in memo:
        return memo[num]
    else:
        memo[num] = fibonacci(num - 1) + fibonacci(num - 2)
        return memo[num]

def find_fibonacci_index_by_length(num):
    fib_num = 1
    while True:
        length = len(str(fibonacci(fib_num)))
        if num == length:
            break

        fib_num += 1

    return fib_num


# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)