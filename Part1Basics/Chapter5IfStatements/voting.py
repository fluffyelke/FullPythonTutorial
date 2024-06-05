age = 16
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 25
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# improved if-elif-else chain
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f'Your admission cost is ${price}.')

age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f'Your admission cost is ${price}.')

alien_color = 'yellow'
if alien_color == 'green':
    points = 5
if alien_color == 'yellow':
    points = 10
print(f'{points}')

if alien_color == 'green':
    points = 5
elif alien_color != 'green':
    points = 10
print(points)

if alien_color == 'green':
    points = 100
else:
    points = 10
print(points)

names = ['alice', 'caprice', 'alaina', 'vanya']
if 'alice' in names:
    print(f'Hello {"alice".title()}')
if 'caprice' in names:
    print(f'Hello {"caprice".title()}')

for name in names:
    if name == 'vanya':
        print(f"Hello, {name.title()} how are you today?")
    else:
        print("Not Here")
print("End")

toppings = []
if toppings:
    for topping in toppings:
        print(f'Do Something')
    print(f"End of the loop")
else:
    print("The List is empty")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")
