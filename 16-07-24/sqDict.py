# Write a program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n = int(input("Enter n: "))
result = dict([(x, x * x) for x in range(1, n + 1)])
print(result)
