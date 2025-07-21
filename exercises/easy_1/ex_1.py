def get_numbers():
    order = ['1st', '2nd', '3rd', '4th', '5th']
    numbers = []

    for idx in range(len(order)):
        numbers.append(input(f"Enter the {order[idx]} number: "))
    
    return numbers

def get_last_num():
    return input("Enter the last number: ")

def display_result(numbers, last_number):
    if last_number in numbers:
        print(f"{last_number} is in {",".join(numbers)}.")
    else:
        print(f"{last_number} isn't in {",".join(numbers)}.")

user_numbers = get_numbers()
last_num = get_last_num()

display_result(user_numbers, last_num)