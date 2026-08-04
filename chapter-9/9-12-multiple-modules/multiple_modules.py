# 9.12(a) Multiple Modules

from user_class import User
from admin_child_class import Admin
from privileges_child_class import Privileges

hatsune = Admin(
    "Miku", "Hatsune", 16, "Your Wi-Fi", "Based", ['Can delete posts', 
                                                   'Can ban users', 
                                                   'Can create groups',])


hatsune.greet_user()
hatsune.describe_user()
hatsune.increment_login_attempts()
print(f"Login attempts: {hatsune.login_attempts}")
hatsune.privileges.show_privileges()