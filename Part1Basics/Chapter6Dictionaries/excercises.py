people = []

vanya = {
    'first': 'vanya',
    'last': 'dimitrova',
    'age': 36,
    'city': 'karnobat'
}

pepo = {
    'first': 'petar',
    'last': 'georgiev',
    'age': 35,
    'city': 'sofia'
}

joro = {
    'first': 'georgi',
    'last': 'slavov',
    'age': 37,
    'city': 'sofia'
}
people.append(vanya)
people.append(pepo)
people.append(joro)

for names in people:
    full_name = f"{names['first'].title()} {names['last'].title()}"
    print(f"{full_name}")
    for key, value in names.items():
        print(f"\t\t{key}: {value}")

print()
for names in people:
    for atrib, atrib_value in names.items():
        print(f"\t\t{atrib}: {atrib_value}")

