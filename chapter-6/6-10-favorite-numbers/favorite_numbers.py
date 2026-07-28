# 6.10 Favorite Numbers

numbers = {
    'Oziel': [8, 4, 0],
    'Jhin': [4, 44, 444, 4444],
    'Beast': [666, 999],
    'Miku': [39, 1],
    }

for name, nums in numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for num in nums:
        print(f"- {num}")

print()