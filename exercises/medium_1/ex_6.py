"""
P
Determine whether a positive integer is a prime number (divisor of 1 and itself only) and return a boolean value

E
- 1 is not a prime number
- input is postive integer

D
input: integer
output: boolean value
intermediate: list to store divisors

A
- return False if input is 1
- iterate from 1 to half of number and check if each number is evenly divisible by number
    - if evenly divisible, store number in a divisor list
- if length of list is 1, return True, else return False

1. Initialize an empty list 'divisor'
2. return False if input is 1
3. Iterate from range of 1 to input // 2
    - if evenly divisible by input, store number in 'divisor'
4. If length of list is 1, return True, else return False
"""

def is_prime(number):
    if number == 1:
        return False

    for num in range(2, (number // 2) + 1):
        if number % num == 0:
            return False

    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True