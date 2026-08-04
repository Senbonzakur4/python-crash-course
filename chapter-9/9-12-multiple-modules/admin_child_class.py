# 9.12(c) Multiple Modules

from user_class import User
from privileges_child_class import Privileges

class Admin(User):
    """A model for admin users"""
    def __init__(self, first_name, last_name, age, locality, favorite_language,
                 privileges):
        super().__init__(first_name, last_name, age, locality, favorite_language)
        self.privileges = Privileges(privileges)