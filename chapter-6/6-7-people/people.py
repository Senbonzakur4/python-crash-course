# 6.7 People

person1 = {
    'first_name': 'Miku',
    'last_name': 'Hatsune',
    'age': 16,
    'height': 158,
    'weight': 42,
    'region': 'Hokkaido',
    }

person2 = {
    'first_name': 'Oziel',
    'last_name': 'Velazquez',
    'age': 27,
    'height': 178,
    'weight': 65,
    'region': 'Nuevo Leon',
    }

person3 = {
    'first_name': 'Khada',
    'last_name': 'Jhin',
    'age': 'Classified',
    'height': 'Classified',
    'weight': 'Classified',
    'region': 'Ionia',
}

people = [person1, person2, person3]

for person in people:
    print(f"\nPersonal Information:")
    for key, value in person.items():
        print(f"{key}: {value}")

print()