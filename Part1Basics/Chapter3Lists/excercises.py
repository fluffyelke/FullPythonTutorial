names = ['alaina', 'caprice', 'vanya', 'elinna', 'elvira']
print(f"Would you wanna join me for a dinner, {names[0].title()}?")
print(f"Would you wanna join me for a dinner, {names[1].title()}?")
print(f"Would you wanna join me for a dinner, {names[2].title()}?")
print(f"Would you wanna join me for a dinner, {names[3].title()}?")
print(f"Would you wanna join me for a dinner, {names[4].title()}?")
print(f"{names[4].title()}, wont be able to join us.")
names[4] = 'deska'
print(f"Would you wanna join me for a dinner, {names[0].title()}?")
print(f"Would you wanna join me for a dinner, {names[1].title()}?")
print(f"Would you wanna join me for a dinner, {names[2].title()}?")
print(f"Would you wanna join me for a dinner, {names[3].title()}?")
print(f"Would you wanna join me for a dinner, {names[4].title()}?")
print("We have room for 3 more for the dinner")
names.append('pepo')
names.append('umi')
names.append('remu')
names.insert(0, 'andrea')
names.insert(5, 'jivo')
print(names)
print("Time for only 2 in the list")
print(f'Sorry, {names.pop().title()}, you have to leave the party')
print(f'Sorry, {names.pop().title()}, you have to leave the party')
print(f'Sorry, {names.pop().title()}, you have to leave the party')
print(f'Sorry, {names.pop().title()}, you have to leave the party')
print(f'Sorry, {names.pop().title()}, you have to leave the party')
print(f'Sorry, {names.pop().title()}, you have to leave the party')
print(f'Sorry, {names.pop().title()}, you have to leave the party')
print(names)
del names[2]
del names[1]
del names[0]
print(len(names))

names = ['vanya', 'elinna', 'caprice', 'alaina', 'deska']
print(names)
names.sort()
print(names)

# sort in reverse
names.sort(reverse=True)
print(names)

# temporary sort
print('Temp sort 2: ')
print(sorted(names))
print('After temp sort 2')
print(names)

print('Temp sort: ')
print(sorted(names, reverse=True))
print('After temp sort')
print(names)

names.reverse()
print(names)

places = ['bulgaria', 'greece', 'columbia', 'england', 'germany']
print(places)
print(len(places))
print(sorted(places))
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)