def leading_substrings(text):
    return [text[:i] for i in range(1, len(text) + 1)]

def substrings(text):
    result = []
    for i in range(len(text)):
        result.extend(leading_substrings(text[i:]))

    return result

def palindromes(text):
    return [substring for substring in substrings(text)
                      if len(substring) > 1 and substring == substring[::-1]]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True