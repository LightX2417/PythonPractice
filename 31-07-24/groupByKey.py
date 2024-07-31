# Write a program to group elements of a list by their first letter using itertools.groupby.

import itertools

elements = ["apple", "apricot", "banana", "cherry", "blueberry", "avocado"]
elements.sort()  # groupby requires the data to be sorted

grouped = itertools.groupby(elements, key=lambda x: x[0])

print("Grouped elements by their first letter:")
for key, group in grouped:
    print(key, list(group))
