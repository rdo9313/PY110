def swap_name(name):
    first_name, last_name = name.split(" ")
    return f"{last_name}, {first_name}"

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True