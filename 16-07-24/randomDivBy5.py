# Write a program to generate 3 random integers between 100 and 999 which are divisible by 5.

import random

nums = random.sample([x for x in range(100, 1000) if x % 5 == 0], k=3)
print(nums)
