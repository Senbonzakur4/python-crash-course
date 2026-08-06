# 10.2 Learning C

from pathlib import Path

path = Path('chapter-10/10-0-chapter-resources/learning_python.txt')

content = path.read_text()

print(f"\nShowing 'learning_python.txt' file using .replace():")

for line in content.splitlines():
    print(line.replace('Python', 'C'))