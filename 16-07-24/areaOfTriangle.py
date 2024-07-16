# Write a python program to find the area of a triangle whose sides are given.

from math import sqrt

def areaoftriangle(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))

a, b, c = tuple([int(input(f"Side {x+1}: ")) for x in range(3)])
print(f"The area of the Triangle is {areaoftriangle(a,b,c)}")
