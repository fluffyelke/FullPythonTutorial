message = input("Tell me something, and i will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name.title()}!")

number = int(input("How Old Are you? "))
print(number)    # actually is string and not a int so we have to cast it to int

if number >= 25:
    print("True")
