current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nTell me something, or Enter 'quit' to end the program. "

# using a flag
active = True
while active:
    message = input(prompt)
    if message.lower() == 'quit':
        active = False
    else:
        print(message)
