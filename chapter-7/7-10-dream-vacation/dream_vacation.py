# 7.10 Dream Vacation

dreamed_place = {}

while True:
    name = input("\nWhat's your name?\n(Type ENTER to exit) ").title()
    if name == '':
        break
    place = input(f"If you could visit one place in the world, where would you"
                  f"go, {name}: ").title()
    dreamed_place[name] = place

print()

for name, place in dreamed_place.items():
    print(f"{name} wants to go to {place}.")

print()