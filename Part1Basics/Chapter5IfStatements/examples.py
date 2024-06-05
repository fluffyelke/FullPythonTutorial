cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print("Continue")

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

first = 22
second = 25
if first >= 20 and second >= 24:
    print("Both are True")

first = 15
second = 25
if first >= 20 or second >= 20:
    print("First or Second is True")

# check if value is in the list.
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("Mushrooms Exists")
else:
    print("Mushrooms didn't exists")

if 'pepperoni' in requested_toppings:
    print("Pepperoni exists")
else:
    print("Pepperoni didn't exist")

# check if valus is not in the list.
banned_users = ['andrew', 'alaina', 'caprice']
user = 'veronica'

if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')

# boolean expressions
game_active = True
print(game_active)
