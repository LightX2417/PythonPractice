# Write a Python program to combine two dictionaries adding values for common keys.

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "c": 500, "d": 400}
combined = {}
for x, y in d1.items():
    combined[x] = y
for x, y in d2.items():
    if x in combined:
        combined[x] += y
    else:
        combined[x] = y
print(f"Combined dictionary:\n{combined}")
