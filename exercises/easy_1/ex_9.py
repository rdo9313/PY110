def string_to_integer(text):
    result = 0

    for idx, digit in enumerate(reversed(text)):
        result += (ord(digit) - ord('0')) * 10**idx
    
    return result

def string_to_signed_integer(text):
    if text[0] in "+-":
        sign = -1 if text[0] == "-" else 1
        return sign * string_to_integer(text[1:])
    
    return string_to_integer(text)

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True