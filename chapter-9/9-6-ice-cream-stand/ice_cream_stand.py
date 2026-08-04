# 9.6 Ice Cream Stand

class Restaurant:
    """A simple Restaurant model"""

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant's name is: {self.name}\nAnd its cuisine type is: "
              f"{self.type}.")

    def open_restaurant(self):
        print(f"{self.name} is now open!\n")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


class IceCreamStand(Restaurant):
    """A child class of the Restaurant class"""

    def __init__(self, name, type, ice_flavors):
        super().__init__(name, type)
        self.ice_flavors = ice_flavors

    def display_flavors(self):
        print(f"Flavors in Stock:")
        for flavor in self.ice_flavors:
            print(f"- {flavor}")


flavors = ['Vanilla', 'Chocolate', 'Lemon', 'Choco-Mint', 'Strawberry']
michoacana = IceCreamStand("Michoacana", "Ice Cream Stand", flavors)
print()
michoacana.describe_restaurant()
michoacana.open_restaurant()
michoacana.display_flavors()