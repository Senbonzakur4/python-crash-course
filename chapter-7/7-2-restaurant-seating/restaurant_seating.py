# 7.2 Restaurant Seating

people = input("\nHow many people are in your dinner group? ")
people = int(people)

if people > 8:
    print("You'll have to wait for a table.\n")
else:
    print("Your table is ready!\n")