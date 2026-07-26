# 5.9. No Users

users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"\nHello {user.title()}, would you like to see a status report?")
        else:
            print(f"\nHello {user.title()}, thank you for logging in again.")
else:
    print("\nWe need to find some users!")

print()