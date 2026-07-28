# 7.6 Three Exits

topping = ''
count = 1

while count < 11:
    topping = input(f"\nWelcome, enter a pizza topping or type 'quit' to exit the"
    f"program\nYou can add {11 - count} more toppings. ")

    if topping == 'quit':
        break
    else:
        print(f"\nAdding {topping} to your pizza...")

    count += 1

print("\nYour pizza is ready!\n ")