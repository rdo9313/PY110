def integer_to_string(number):
    result = ''
    digits = '0123456789'

    while True:
        number, remainder = divmod(number, 10)
        result = digits[remainder] + result
        
        if number == 0:
            break
    
    return result

print(integer_to_string(4321) == "4321")              # True
print(integer_to_string(0) == "0")                    # True
print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) == "1234567890")  # True