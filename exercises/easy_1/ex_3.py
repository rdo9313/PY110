def is_palindrome(string):
    return string == string[::-1]

def is_real_palindrome(string):
    alnum_string = "".join([char for char in string.lower() if char.isalnum()])
    return is_palindrome(alnum_string)

print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True
print(is_real_palindrome('Madam') == True)           # True
print(is_real_palindrome("Madam, I'm Adam") == True) # True