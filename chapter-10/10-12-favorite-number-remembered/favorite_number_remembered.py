# 10.12 Favorite Number Remembered

from pathlib import Path
import json

path = Path('chapter-10/10-0-chapter-resources/number_remembered.json')

if path.exists():
    content = path.read_text()
    number = json.loads(content)
    print(f"\nI know your favorite number! It's: {number}\n")

else:
    number = int(input(f"\nWhat's your favorite number?: "))
    content = json.dumps(number)
    path.write_text(content)
    print(f"I'll remember your favorite number.\n")