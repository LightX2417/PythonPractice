# Write a program to generate random String of length entered by the user. String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol except single space.

import random

values = (
    [chr(x) for x in range(ord("A"), ord("Z") + 1)]
    + [chr(x) for x in range(ord("a"), ord("z") + 1)]
    + [" "]
)
n = int(input("Enter the length of the string: "))
string = random.choices(values, k=n)
string = "".join(string)
print(string)
