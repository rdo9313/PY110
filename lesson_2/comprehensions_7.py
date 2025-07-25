lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

new_lst = []
for el in lst:
    multiples_of_3 = []
    
    for number in el:
        if number % 3 == 0:
            multiples_of_3.append(number)

    new_lst.append(multiples_of_3)

print(new_lst == [[], [3, 12], [9], [15, 18]])

    
def divisible_by_3(sublist):
    return [num for num in sublist if num % 3 == 0]

new_lst = [divisible_by_3(sublist) for sublist in lst]

print(new_lst == [[], [3, 12], [9], [15, 18]])