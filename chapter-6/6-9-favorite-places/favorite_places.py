# 6.9 Favorite Places

favorite_places = {
    'Oziel': ['Russia', 'Japan', 'Mexico'],
    'Miku': ['Your Wi-Fi', 'Brasil', 'Japan'],
    'Geralt': ['Kaer Morhen', 'Novigrad', 'Skellige'],
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")

print()