# 6.11 Cities

cities = {
    'Saint Petersburg': {
        'country': 'Russia',
        'population': 5383890,
        'fact': 'Saint Petersburg is known for its beautiful architecture and cultural '
        'heritage.',
    },
    'Sapporo': {
        'country': 'Japan',
        'population': 1920000,
        'fact': 'Sapporo is the largest city in Hokkaido and is known for its beer and '
        'snow festivals.',
    },
    'Monterrey': {
        'country': 'Mexico',
        'population': 1135512,
        'fact': 'Monterrey is a major industrial and business center in northern '
        'Mexico.',
    },
}

for city, info in cities.items():
    print(f"\nHere's some info about {city}:")
    for fact, description in info.items():
        print(f"- {fact}: {description}")

print()
