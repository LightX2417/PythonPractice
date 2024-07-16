# Write a Python program to calculate surface volume and area of a sphere.

from math import *

r = float(input("Enter radius of the sphere : "))
surfacearea = 4 * pi * pow(r, 2)
volume = (4 / 3) * pi * pow(r, 3)
print(f"Surface area of the sphere: {surfacearea} units\u00b2")
print(f"Volume of the sphere: {volume} units\u00b3")
