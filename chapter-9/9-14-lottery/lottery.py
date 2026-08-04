# 9.14 Lottery

from random import choice

lottery = ['1', 'A', '2', 'B', '3', 'C', '4', 'D', '5', 'E', '6', 'F', '7', 'G', '8']

print(f"\nWelcome!, Any ticket ticket matching these 4 characters win a prize:")
for i in range(4):
    print(f"- {choice(lottery)}")