import random

numerical_list = []
for value in range(1, 10):
    print(value, end=" ")
    numerical_list.append(value)

print()
print(numerical_list)
new_list = []
for val in numerical_list:
    val *= val
    new_list.append(val)
print(new_list)

# making list of numbers
numbers = list(range(1, 11))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)
random.shuffle(squares)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# list comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)

print(list(range(1, 21)))

million_numbers = list(range(1, 1_000_001))
# print(million_numbers)
# for val in million_numbers:
#    print(val)

print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))

odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

odd_numbers = []
for val in range(1, 11):
    odd_numbers.append(val ** 3)

print(odd_numbers)

odd_numbers = [value ** 4 for value in range(1, 11)]
print(odd_numbers)


ex_list = list(range(1, 11))
print(ex_list)

print(f'The first  three elements in the list are: ')
print(ex_list[0:3])

print(f"Three items from the middle of the list are: ")
print(ex_list[3:7])

print(f"The last three items in the list are: ")
print(ex_list[-3:])