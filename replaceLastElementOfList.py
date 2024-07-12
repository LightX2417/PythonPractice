# Write a Python program to replace the last 
# element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]


l1=[eval(input(f"l1[{x}]")) for x in range(5)]
l2=[eval(input(f"l2[{x}]")) for x in range(5)]
print(f"l1={l1}")
print(f"l2={l2}")
l1.pop()
l1.extend(l2)
print(f"l1={l1}")

