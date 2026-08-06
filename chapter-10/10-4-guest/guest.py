# 10.4 Guest

from pathlib import Path

path = Path('chapter-10/10-0-chapter-resources/guest.txt')

prompt = input(f"\nHi, write something: ")
path.write_text(prompt)
print(f"A file called 'guest.txt' in [ {path} ] has been created.\n")