# 7.8 Deli

sandwich_order = ['Tuna', 'Pastrami', 'Chicken', 'Veggie']
finished_sandwiches = []

print()
while sandwich_order:
    sandwich = sandwich_order.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nSandwiches made:")
for finished in finished_sandwiches:
    print(f"- {finished} sandwich")

print()