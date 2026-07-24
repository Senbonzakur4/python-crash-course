# 3.8. Seeing the World

locations = ["japan", "russia", "germany", "spain", "norway"]

print(f"\nOriginal List: {locations}")
print(f"Sorted List in Alphabetical Order: {sorted(locations)}")

print(f"\nOriginal List: {locations}")
print(f"Sorted List in Reverse Alphabetical Order: {sorted(locations, reverse = True)}")
print(f"Original List: {locations}")

locations.reverse()
print(f"\nReversed List: {locations}")
locations.reverse()
print(f"Reversed List so it is back to the original order: {locations}")

locations.sort()
print(f"\nSorted List: {locations}")
locations.sort(reverse = True)
print(f"Sorted List in Reverse Alphabetical Order: {locations}\n")
