# 10.1 Learning Python

from pathlib import Path

path = Path('chapter-10/10-0-chapter-resources/learning_python.txt')

content = path.read_text()

print(f"\nHere is the full text:\n{content}\n\nHere is the text line by line:")
for line in content.splitlines():
    print(f"- {line}")