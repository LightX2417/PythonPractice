# Write a Python program to calculate the area of regular polygon.

import math

def area_of_polygon(n, s):
    return (n * pow(s, 2)) / (4 * math.tan(math.pi / n))

sides = float(input("Enter number of sides: "))
length = float(input("Enter length of side: "))

area = area_of_polygon(sides, length)
print(area)
