# Write a Python program to convert string values of a given dictionary, into integer datatypes

ol = [{"x": "10", "y": "20", "z": "30"}, {"p": "40", "q": "50", "r": "60"}]
nl = []
for x in ol:
    for a, b in x.items():
        x[a] = int(b)
    nl.append(x)
print(f"New List:\n{nl}")
