# 9.10(b) Import Restaurant

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