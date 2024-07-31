# Write a program to generate all possible combinations of a given list of elements taken two at a time.

import itertools

elements = ["A", "B", "C", "D"]
combinations = list(itertools.combinations(elements, 2))

print("All combinations taken two at a time:")
print(combinations)
