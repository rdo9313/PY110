"""
P
Return the nth fibonacci number where n is the argument passed in

E
F(1) = 1
F(2) = 1
F(n) = F(n - 1) + F(n - 2)    (where n > 2)

D
input: integer
output: integer

A
- Set input numbers 1 and 2 to the values 1
- Create a list with previous, current values
- for each iteration in range from 3 to input + 1, add previous to current values
- return current value
"""

def fibonacci(num):
    if num in (1, 2):
        return 1

    prev = 1
    current = 1
    for _ in range(3, num + 1):
        prev, current = current, prev + current

    return current


print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True