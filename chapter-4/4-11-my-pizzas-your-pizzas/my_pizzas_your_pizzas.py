# 4.11. My Pizzas, Your Pizzas

my_pizzas = ['peperoni', 'mexican', '4 meats']
friend_pizzas = my_pizzas[:]

my_pizzas.append('Fish')
friend_pizzas.append('Hawaian')

print(f"\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print(f"\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

print()