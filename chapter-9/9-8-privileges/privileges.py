# 9.8 Privileges

class User:

    def __init__(self, first_name, last_name, age, locality, favorite_language):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.locality = locality
        self.favorite_language = favorite_language
        self.login_attempts = 0

    def describe_user(self):
        print(
            f"User Info:\nFirst Name: {self.first_name}\n"
            f"Last Name: {self.last_name}\n"
            f"Age: {self.age}\nLocality: {self.locality}\n"
            f"Favorite Language: {self.favorite_language}\n"
        )

    def greet_user(self):
        print(f"\nWelcome! {self.first_name} {self.last_name}.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """A model for admin users"""
    def __init__(self, first_name, last_name, age, locality, favorite_language,
                 privileges):
        super().__init__(first_name, last_name, age, locality, favorite_language)
        self.privileges = Privileges(privileges)


class Privileges:
    """A privileges Parent class"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Admin users can: ")
        for privilege in self.privileges:
            print(f"- {privilege}")


hatsune = Admin(
    "Miku", "Hatsune", 16, "Your Wi-Fi", "Based", ['Can delete posts', 
                                                   'Can ban users', 
                                                   'Can create groups',])

print(f"\nUsing the Privileges class to show the privileges of the Admin child class:")
hatsune.privileges.show_privileges()