# 9.12(d) Multiple Modules

class Privileges:
    """A privileges Parent class"""

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Admin users can: ")
        for privilege in self.privileges:
            print(f"- {privilege}")