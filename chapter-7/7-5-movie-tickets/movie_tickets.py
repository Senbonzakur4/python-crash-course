# 7.5 Movie Tickets

age = 0

while True:
    age = int(input("\nWelcome, type your age to buy a ticket:\n"
    "(Type '-1' to exit)"))

    if 0 <= age < 3:
        print("\nYour ticket is free!")
    elif 3 <= age < 12:
        print("\nYour ticket costs $10")
    elif age >= 12:
        print("\nYour ticket costs $15")
    else:
        break
    