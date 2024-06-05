magicians = ['alice', 'caprice', 'vanya', 'elvira', 'alaina']

for mag in magicians:
    print(mag)
    print(f"{mag.title()}, that was a great trick")

# outside the for loop
print(f"And we are done.")

pizzas = ['quatro stracioni', 'chorisso', 'ham', 'cheese']
print(pizzas)

for pizza in pizzas:
    print(f"I Like {pizza.title()} pizza.")
print("I really like hot pizza")

animals = ['cat', 'tiger', 'lion', 'boar']

for animal in animals:
    print(f'A {animal.title()}', end=" ")
    print(f'would make a great pet')
print(f'Any of these animals would make a great pet!')


# copying the list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My Favorite Foods are: ")
print(my_foods)

print(f"\nFriend's favorite foods are: ")
print(friend_foods)

my_foods.append('caprice')
friend_foods.append('strawberry')

print(my_foods)
print(friend_foods)

# next example the new list points to the old one.
old_list = ['one', 'two', 'three', 'four']
new_list = old_list

print(old_list)
print(new_list)

old_list.append('five')
new_list.append('six')
print(old_list)
print(new_list)

temp_list = ['vanya', 'elvira', 'caprice', 'alaina']
new_temp = temp_list[:]
temp_list.append('clover')
new_temp.append('four leave')
print(temp_list)
print(new_temp)

for elem in temp_list:
    print(f"Favorite members in temp_list are {elem.title()}")

for elem in new_temp:
    print(f"New List members {elem.title()}")


