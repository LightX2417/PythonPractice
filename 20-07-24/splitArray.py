# Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.

import numpy as np

array = np.arange(10, 34).reshape(8, 3)
print(array)
sub_arrays = np.split(array, 4)
print(sub_arrays[0])
print(sub_arrays[1])
print(sub_arrays[2])
print(sub_arrays[3])
