responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input(f"Which mountain you climb? ")

    # store the response in the dictionary.
    responses[name] = response

    repeat = input("Would you like to let another person respons (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")