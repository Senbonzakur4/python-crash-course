# 10.13 User Dictionary

from pathlib import Path
import json

path = Path('chapter-10/10-0-chapter-resources/user_dictionary.json')
user_info = {}


user_info['first name'] = input(f"\nHi, what's your first name?: ").title()
user_info['last name'] = input(f"What's your last name?: ").title()
user_info['age'] = input(f"How old are you?: ")

content = json.dumps(user_info)
path.write_text(content)

print(f"\nI stored your user info in a .json file\nHere's what I stored:\n")

content = path.read_text()
user_info2 = json.loads(content)

for key, value in user_info2.items():
    print(f"{key.title()}: {value}")
print()