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

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True