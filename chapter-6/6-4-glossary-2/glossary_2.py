# 6.4 Glossary 2

glossary = {
    'string': 'A series of characters.',
    'for': 'A loop that iterates over a sequence.',
    'list': 'A collection of items in a particular order.',
    'tuple': 'An immutable collection of items in a particular order.',
    'dictionary': 'A collection of key-value pairs.',
    'set': 'An unordered collection of unique items.',
    'boolean': 'A data type that can have one of two values: True or False.',
    'key': 'A unique identifier used to access a value in a dictionary.',
    'value': 'The data associated with a key in a dictionary.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")