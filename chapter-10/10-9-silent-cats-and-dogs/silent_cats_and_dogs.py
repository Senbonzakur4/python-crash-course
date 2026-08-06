# 10.9 Silent Cats and Dogs

from pathlib import Path


try:
    """Changed the file name 'dogs.txt' to catch the FileNotFoundError exception."""
    path1 = Path('chapter-10/10-0-chapter-resources/cats.txt')
    path2 = Path('chapter-10/10-0-chapter-resources/dogz.txt')

    content1 = path1.read_text()
    print("\nContent of cats.txt:")
    print(content1)

    content2 = path2.read_text()
    print("\nContent of dogs.txt:")
    print(content2)

except FileNotFoundError:
    pass  # Silently ignore the error and do nothing