def count_occurrences(lst):
    for el in set(lst):
        print(f"{el} => {lst.count(el)}")

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)