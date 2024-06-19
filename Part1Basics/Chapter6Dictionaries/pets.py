pets = []

shlupcho = {
    'type': 'cat',
    'age' : 12,
    'owner': 'joro',
}

mangala = {
    'type': 'cat',
    'age': 5,
    'owner': 'pepo',
}

sparki = {
    'type': 'dog',
    'age': 3,
    'owner': 'vanya',
}
pets.append(shlupcho)
pets.append(mangala)
pets.append(sparki)

for elements in pets:
    for k, v in elements.items():
        print(f"\t\t{k}: {v}")

favotite_places = {
    'vanya': ['bulgaria', 'turkey', 'india', 'france'],
    'georgi': ['malta', 'iran', 'china'],
    'pepo': ['italy', 'iran', 'bolivia', 'columbia'],
}
for k, v in favotite_places.items():
    print(f"\t{k.title()}")
    for places in v:
        print(f"\t\t{places.title()}")

cities = {
    'sofia': {
        'country': 'bulgaria',
        'population': 1_500_000,
        'fact': 'The city is very old',
    },
    'paris': {
        'country': 'france',
        'population': 6_500_000,
        'fact': 'the francofolies',
    },
    'berlin': {
        'country': 'germany',
        'population': 8_500_000,
        'fact': 'brandenburg door',
    },
}

for k,v in cities.items():
    print(f"\t{k.title()}")
    for key, value in v.items():
        print(f"\t\t{key}: {value}")
