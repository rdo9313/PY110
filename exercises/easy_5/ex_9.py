def staggered_case(text):
    result = ''
    uppercase = True

    for char in text:
        if char.isalpha():
            result += char.upper() if uppercase else char.lower()
            uppercase = not uppercase
        else:
            result += char

    return result