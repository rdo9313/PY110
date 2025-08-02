"""
P
Given a list and a search argument, return index of search item

E
- returns -1 if search item not found
- list argument will always be sorted

D
input: list, string
output: integer

A
1. set high index to len(input) - 1
2. set low index to 0
3. while low <= high, set 'mid' to (high + low) // 2
4. if input[mid] == search, return mid
5. if input[mid] > search, high = mid - 1
6. if input[mid] < serach, low = mid + 1
7. return -1

"""

def binary_search(lst, search):
    high = len(lst) - 1
    low = 0

    while low <= high:
        mid = (high + low) // 2
        if lst[mid] == search:
            return mid
        elif lst[mid] > search:
            high = mid - 1
        else:
            low = mid + 1

    return -1

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)