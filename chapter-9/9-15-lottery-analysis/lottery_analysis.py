# 9.15 Lottery Analysis

from random import choice

lottery = [0, 'Z', 1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E', 6, 'F', 7, 'G', 8, 'H', 9]

pull = []
my_ticket = [0, 'Z', 'Z', 1]

print(f"\nMy ticket is 0-Z-Z-1. Let's see how many tries I need to win:")

tries = 0

while True:
    for i in range(4):
        pull.append(choice(lottery))

    tries += 1

    if pull == my_ticket:
        break
    else:
        pull = []

print(f"Number of tries: {tries}!!!")