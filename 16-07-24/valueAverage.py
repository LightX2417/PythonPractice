# Write a Python program to replace dictionary values with their average.

d1 = {"a": 5, "b": 3, "c": 9, "d": 1}
average = sum(d1.values()) / len(d1.values())
for x in d1:
    d1[x] = average
print(f"New dictionary:\n{d1}")
