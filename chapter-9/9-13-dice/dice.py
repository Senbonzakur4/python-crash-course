# 9.13 Dice

from random import randint

class Die:
    """An attempt to make a die model"""

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(f"{i + 1}.- {randint(1, self.sides)}")

sides = 6
dado6 = Die(sides)
print(f"\n{sides} sides die tries: ")
for i in range (10):
    dado6.roll_die()

sides = 10
dado10 = Die(sides)
print(f"\n{sides} sides die tries: ")
for i in range (10):
    dado10.roll_die()

sides = 20
dado20 = Die(sides)
print(f"\n{sides} sides die tries: ")
for i in range (10):
    dado20.roll_die()