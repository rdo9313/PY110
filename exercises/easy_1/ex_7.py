def swap_word(word):
    return word if len(word) == 1 else (word[-1] + word[1:-1] + word[0])
    
def swap(text):
    return " ".join([swap_word(word) for word in text.split()])

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True