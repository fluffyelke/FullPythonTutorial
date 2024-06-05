usernames = ['vanYa', 'elvIra', 'elinna', 'caprice', 'alaina', 'admin']
# usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello, Master")
        else:
            print(f"Welcome back, {user.title()}")
else:
    print("There are no users")

current_users = usernames[:]        # make a copy to the list
print(current_users)
current_users.append('stella')
print(usernames, current_users)

new_users = ['Elinna', 'Elvira', 'Vanya', 'pepo', 'georgi']
if new_users:
    for user in new_users:
        if user.lower() in current_users:
            print(f"Name {user} is already used please choose another one.")
        else:
            print(f"User name {user} is available")

numbers = list(range(1, 11))
if numbers:
    for num in numbers:
        if num == 1:
            print(f'{num}st')
        elif num == 2:
            print(f"{num}nd")
        elif num == 3:
            print(f"{num}rd")
        else:
            print(f"{num}th")