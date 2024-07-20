# Write a NumPy program to find common values between two arrays.

import numpy as np

array_1 = np.array([0, 10, 20, 40, 60])
array_2 = np.array([10, 30, 40])
result = np.intersect1d(array_1, array_2)
print(result)
