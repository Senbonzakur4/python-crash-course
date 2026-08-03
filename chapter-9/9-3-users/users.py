# 9.3 Users

class User:

    def __init__(self, first_name, last_name, age, locality, favorite_language):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.locality = locality
        self.favorite_language = favorite_language

    def describe_user(self):
        print(
            f"User Info:\nFirst Name: {self.first_name}\n"
            f"Last Name: {self.last_name}\n"
            f"Age: {self.age}\nLocality: {self.locality}\n"
            f"Favorite Language: {self.favorite_language}\n"
        )

    def greet_user(self):
        print(f"\nWelcome! {self.first_name} {self.last_name}.")


oziel = User("Oziel", "Velazquez", 27, "Monterrey", "Python")
miku = User("Miku", "Hatsune", 16, "Your Wi-Fi", "Based")
jhin = User("Khada", "Jhin", "REDACTED", "Ionia", 4444)

oziel.greet_user()
oziel.describe_user()

miku.greet_user()
miku.describe_user()

jhin.greet_user()
jhin.describe_user()