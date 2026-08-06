# 10.11(a) Favorite Number

from pathlib import Path
import json

path = Path('chapter-10/10-0-chapter-resources/number.json')

number = int(input(f"\nWhat's your favorite number?: "))

content = json.dumps(number)
path.write_text(content)