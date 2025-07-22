def double_consonants(text):
    vowels = 'aeiou'
    result = ''

    for char in text:
        if char.isalpha() and char.lower() not in vowels:
            result += char * 2
        else:
            result += char
    
    return result

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")