# 9.5 Login Attempts

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

jhin = User("Khada", "Jhin", "REDACTED", "Ionia", "4444")
print(f"\nLogin Attempts: {jhin.login_attempts}")
jhin.increment_login_attempts()
jhin.increment_login_attempts()
jhin.increment_login_attempts()
jhin.increment_login_attempts()
print(f"Updated Login Attempts: {jhin.login_attempts}")
jhin.reset_login_attempts()
print(f"Reseted Login Attempts: {jhin.login_attempts}\n")