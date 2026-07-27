# 6.8 Pets

cat = {
    'name': 'Mah',
    'type': 'cat',
    'owner': 'Oziel',
}

dog = {
    'name': 'Sesame',
    'type': 'dog',
    'owner': 'Karely',
}

penguin = {
    'name': 'Tux',
    'type': 'penguin',
    'owner': 'Linus'
}

pets = [cat, dog, penguin]

for pet in pets:
    print()
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")

print()