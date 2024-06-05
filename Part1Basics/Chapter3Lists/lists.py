names = ['vanya', 'elvira', 'elinna', 'caprice']
print(names)

print(names[0])

print(names[1].title())

# accessing the last element of the list
print(names[-1])
print(names[-2])

message = f"Hello, {names[2].title()}, welcome to the jungle"
print(message)

names[1] = 'alaina'
print(names)

# adding element to the list using append()

names.append('elvira')
print(names)
names.append(100)
print(names)

# empty list
names = []
names.append('one')
names.append('two')
names.append(3)
names.append(4)
names.append('five')
print(names)

# insert element to the list using insert()
names.insert(2, 'elsa')
print(names)

# remove element from the list
del names[3]
print(names)

# pop element from the list
popped_name = names.pop()   # pop the last element in the list
print(popped_name)
print(names)

popped_name = names.pop(1)  # pop the element on the index 1
print(popped_name)
print(names)

# remove by value
names.remove('one')
print(names)

my_var = 4
names.remove(my_var)
print(names)

# size of the list
print(len(names))