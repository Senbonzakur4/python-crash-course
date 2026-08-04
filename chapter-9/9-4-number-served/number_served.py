# 9.4 Number Served

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

restaurant = Restaurant("Sushi House", "Japanese")
print(f"\nClients Served: {restaurant.number_served}")
restaurant.number_served = 10
print(f"Clients Served Update directly: {restaurant.number_served}")
restaurant.set_number_served(400)
print(f"Clients Served Updated with Method: {restaurant.number_served}")
restaurant.increment_number_served(44)
print(f"Clients Served Incremented with Method: {restaurant.number_served}\n")