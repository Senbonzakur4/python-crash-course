# 9.1(b) Restaurant

class Restaurant:
    """A simple Restaurant model"""

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print(f"The restaurant's name is: {self.name}\nAnd its cuisine type is: "
              f"{self.type}.")

    def open_restaurant(self):
        print(f"{self.name} is now open!\n")