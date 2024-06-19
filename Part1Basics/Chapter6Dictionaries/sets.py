# keep only unique elements. Set
my_set = {'first', 'second', 'third', 'second', 'first', 'fourth'}
print(my_set)

rivers = {
    'nile': 'egypt',
    'iskar': 'bulgaria',
    'dunabe': 'hungary',
}
for river, country in rivers.items():
    print(f"\tThe {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(f"River: {river.title()}")

for country in rivers.values():
    print(f"Contry: {country.title()}")
