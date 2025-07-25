dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def retrieve_colors(food):
    return [color.capitalize() for color in food["colors"]]

def retrieve_size(food):
    return food["size"].upper()

lst = []
for food in dict1.values():
    if food["type"] == "fruit":
        lst.append(retrieve_colors(food))
    if food["type"] == "vegetable":
        lst.append(retrieve_size(food))
        
print(lst == [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"])