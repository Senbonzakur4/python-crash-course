# 2-8. File Extensions

filename = 'python_notes.txt'

print(f"\n Here's the original name of the file: {filename}")
print(f"\n Here's the file with no suffix: {filename.removesuffix(".txt")}")
simple_filename = filename.removesuffix(".txt")
print(f"\n Now, I use a new variable named 'simple_filename' to show the file with no suffix: {simple_filename}.\n")
