# 7.4 Pizza Toppings

topping = ''

while True:
    topping = input("\nEnter a pizza topping\n(Type 'quit' to exit): ")
    if topping == 'quit':
        break
    else:
        print(f"\nAdding {topping} to your pizza.")