# 5.8. Hello Admin

users = ['oziel', 'admin', 'miku', 'stuart', 'karely']

for user in users:
    if user == 'admin':
        print(f"\nHello {user.title()}, would you like to see a status report?")
    else:
        print(f"\nHello {user.title()}, thank you for logging in again.")

print()