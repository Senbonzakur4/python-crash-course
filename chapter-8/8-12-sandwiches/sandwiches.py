# 8.12 Sandwiches


def make_sandwich(*sandwich_items):
    """Print the list of items that have been requested for the sandwich."""
    print("\nMaking a sandwich with the following items:")
    for item in sandwich_items:
        print(f"- {item}")

print()
make_sandwich('ham', 'cheese', 'lettuce', 'tomato')
make_sandwich('turkey', 'bacon', 'avocado')
make_sandwich('peanut butter', 'jelly')
print()