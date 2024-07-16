# Write a code to solve the equation z = |x − y| * (x + y).

import math

x = int(input("x: "))
y = int(input("y: "))
z = math.fabs(x - y) * (x + y)
print(f"z={z}")
