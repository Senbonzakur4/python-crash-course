# 5.10. Checking Usernames

current_users = ['jOHn', 'OzieL', 'mIKU', 'KaReLy', 'stuART']

new_users = ['oziel', 'miKu', 'josE', 'MurdocK', 'Aaron']

case_sensitive = []

for current_user in current_users:
    case_sensitive.append(current_user.title())

for new_user in new_users:
    if new_user.title() in case_sensitive:
        print(f"\nYou have to choose a different username.")
    else:
        print(f"\nThe username is available.")