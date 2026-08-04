# 9.11(a) Imported Admin

from user_class import User, Admin, Privileges

hatsune = Admin(
    "Miku", "Hatsune", 16, "Your Wi-Fi", "Based", ['Can delete posts', 
                                                   'Can ban users', 
                                                   'Can create groups',])

hatsune.privileges.show_privileges()