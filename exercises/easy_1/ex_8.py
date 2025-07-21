def string_to_integer(text):
    result = 0

    for idx, digit in enumerate(reversed(text)):
        result += (ord(digit) - 48) * 10**idx
    
    return result
    

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True