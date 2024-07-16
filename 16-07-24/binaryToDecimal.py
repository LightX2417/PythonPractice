# Write a Python program to convert a binary number to decimal number.

from math import pow


def bintodec(binarynumber):
    digits = binarynumber.split()
    decimal = 0
    for i in range(len(binarynumber)):
        j = len(binarynumber) - 1 - i
        decimal += int(binarynumber[j]) * pow(2, i)
    return decimal


n = input("Input a binary number: ")
print(f"Decimal Equivalent of {n} is {bintodec(n)}")
