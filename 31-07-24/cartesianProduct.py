# Write a program to compute the Cartesian product of multiple lists.

import itertools

list1 = [1, 2]
list2 = ["A", "B"]
list3 = ["X", "Y"]

cartesian_product = list(itertools.product(list1, list2, list3))

print("Cartesian product of the lists:")
print(cartesian_product)
