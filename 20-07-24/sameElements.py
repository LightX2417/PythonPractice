# Write a NumPy program to test whether each element of a 1-D array is also present in a second array.

import numpy as np

array_1 = np.array([0, 10, 20, 40, 60])
array_2 = np.array([0, 40])
result = np.isin(array_1, array_2)
print(f"Array1:\n{array_1}")
print(f"Array2:\n{array_2}")
print("Compare each element of array1 and array2:")
print(result)