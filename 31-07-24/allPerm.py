# Write a program to generate all possible permutations of a given list of elements.

import itertools

elements = ["A", "B", "C"]
permutations = list(itertools.permutations(elements))

print("All permutations:")
print(permutations)
