# Write a program to sort (ascending and descending) a dictionary by value.

d1 = {"a": 5, "b": 3, "c": 9, "d": 1}
values = list(d1.values())
keys = list(d1.keys())
dasc = dict(sorted(d1.items(), key=lambda item: item[1]))
ddesc = dict(sorted(d1.items(), key=lambda item: item[1], reverse=True))
print(f"Sorted in ascending order: {dasc}")
print(f"Sorted in descending order: {ddesc}")
