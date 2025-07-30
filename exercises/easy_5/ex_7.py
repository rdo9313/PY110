def sum_digits(num):
    digits = []
    while True:
        num, digit = divmod(num, 10)
        digits.append(digit)
        if num == 0:
            break

    return sum(digits)



print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True