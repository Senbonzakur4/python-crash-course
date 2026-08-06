# Chapter 10. Files and Exceptions

## Concepts Learned

- Reading from a File
- Working with File Contents
- Writing to a File
- Try and Except Blocks
- Raising Exceptions
- Handling Exceptions
- Silently Handling Exceptions


## Before running the code

Some exercises use external files (such as `.txt` files). If you want to run those exercises on your own computer, you will need to update the file paths to match the location of the files on your system.

For example, in Exercise 10-10, the code expects `anna_karenina.txt` to be located at:

```text
chapter-10/10-0-chapter-resources/anna_karenina.txt
```

If you save the file somewhere else, update the `Path` object accordingly. For example:

```python
from pathlib import Path

path = Path("C:/Users/<your_username>/Documents/<your_directory>/anna_karenina.txt")
```

You can download `anna_karenina.txt`, or any other public domain text, from Project Gutenberg [Here](https://www.gutenberg.org/ebooks/1399)