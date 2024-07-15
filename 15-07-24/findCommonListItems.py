# Write a Python program to find common items from two lists.

l1 = eval(input("Enter a list"))
l2 = eval(input("Enter a list"))
common = list(set(l1) & set(l2))
print(f"Common elements in both the lists:\n{common}")
