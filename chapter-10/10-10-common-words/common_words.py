# 10.10 Common Words

from pathlib import Path

path = Path('chapter-10/10-0-chapter-resources/anna_karenina.txt')

book_contents = path.read_text(encoding='utf-8')

print(f"\nThis program analyzes Leo Tolstoy's book 'Anna Karenina' from "
      "Project Gutenberg library.\n"
      f"Number of times the word 'Anna' appears in the book: "
      f"{book_contents.count('Anna')}\n")