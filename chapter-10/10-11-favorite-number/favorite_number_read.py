# 10.11(b) Favorite Number

from pathlib import Path
import json

path = Path('chapter-10/10-0-chapter-resources/number.json')

content = path.read_text()
number = json.loads(content)

print(f"\nI know your favorite number! It's: {number}\n")