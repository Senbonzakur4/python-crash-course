# 10.5 Guest Book

from pathlib import Path

path = Path('chapter-10/10-0-chapter-resources/guest_book.txt')

guests = ''
while True:
    prompt = input(f"Hi, write your name or press Enter to quit: ")
    if prompt != '':
        guests += f"{prompt}\n"
    else:
        break

path.write_text(guests)
print(f"\nA file called 'guest_book.txt' in [ {path} ] has been created.\n")