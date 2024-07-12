# Write a Python program to convert a given list of tuples to a list of lists.
# Original list of tuples: [(1, 2), (2, 3), (3, 4)]
# Convert the said list of tuples to a list of 
# lists: [[1, 2], [2, 3], [3, 4]]

l1=[(eval(input("Enter x:")),eval(input("Enter y:"))) for x in range(3)]
print(l1)
l2=[list(x) for x in l1]
print(l2)