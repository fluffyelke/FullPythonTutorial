alien_0 = {'color': 'green',
           'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print(alien_0)
print("Aliens")
print()
aliens = {
    'first': {
      'color': 'green',
      'points': 5
    },
    'second': {
        'color': 'yellow',
        'points': 10
    }
}
for alien, values in aliens.items():
    print('\t', alien)
    for elem in values:
        print('\t\t', elem + ' : ', values[elem])

alien = aliens.get('first')
print(alien['points'])

# add more properties to the 1 alien
alien['x_pos'] = 0
alien['y_pos'] = 25
print(alien)

for alien, values in aliens.items():
    print('\t', alien)
    for elem in values:
        print('\t\t', elem + ' : ', values[elem])


# empty dictioniary
alien_0 = {}

alien_0['color'] = 'red'
alien_0['points'] = 25
print(alien_0)
print(aliens.get('first'))

# modifiyng a dictioniary
my_dict = {'color': 'red'}
print(f"The object color is {my_dict['color']}.")
my_dict['color'] = 'yellow'
print(f"The object color is now {my_dict['color']}.")


alien_0 = {'x_pos': 0, 'y_pos': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_pos']}")

# move the alien to the right.
# determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_pos'] = alien_0['x_pos'] + x_increment
print(f"New position: {alien_0['x_pos']}")

# removing key-value pairs
alien_0 = {'color': 'green',
           'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {
    'first': 'python',
    'second': 'c',
    'third': 'ruby',
    'fourth': 'java',
}

language = favorite_languages.get('first').title()
print(f'First language is {language}.')

language = favorite_languages.get('fifth', 'The "fifth" key doesnt exist')
print(f"Favorite Langage {language}")

person = {
    'first_name': 'vanya',
    'second_name': 'dimitrova',
    'age': 35,
    'city': 'karnobat',
}

print(f'person: \n\t'
      f'first name: {person.get("first_name").title()} \n\t'
      f'second name: {person.get("second_name").title()} \n\t'
      f'age: {person.get("age")} \n\t'
      f'city: {person.get("city")} \n\t')

favotite_numbers = {
    'caprice': 32,
    'vanya' : 37,
    'elvira': 37,
    'pepo': 36,
    'alaina': 25,
}

for name, number in favotite_numbers.items():
    print(f"\t{name}: {number}")
    # print(f"\t\t{number}")

# loopin through dictionary

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}\nValue: {value}")
    