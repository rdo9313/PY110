munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

total_age = 0
for value in munsters.values():
    if value["gender"] == "male":
        total_age += value["age"]

print(total_age)

total_age = sum([value["age"] for value in munsters.values() if value["gender"] == "male"])
print(total_age)