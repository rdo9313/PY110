DIGITS = '0123456789'

def integer_to_string(number):
    result = ''

    while True:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result
        
        if number == 0:
            break
    
    return result

def signed_integer_to_string(number):
    if number == 0:
        return '0'
    
    sign = "+" if number > 0 else "-"
    return sign + integer_to_string(abs(number))

print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True