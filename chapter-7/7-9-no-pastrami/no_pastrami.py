# 7.9 No Pastrami

sandwich_order = ['tuna', 'pastrami', 'chicken','pastrami', 'veggie', 'double',
                  'pastrami']

finished_sandwiches = []

print(f"\nCurrent orders:\n{sandwich_order}\n"
      "Deli has run out of pastrami.\n")

while sandwich_order:
    sandwich = sandwich_order.pop(0)

    if sandwich.title() == 'Pastrami':
        continue
    else:
        print(f"I made your {sandwich.title()} sandwich.")
        finished_sandwiches.append(sandwich.title())

print("\nSandwiches made:")
for finished in finished_sandwiches:
    print(f"- {finished} sandwich")

print()