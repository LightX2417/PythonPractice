# Find indices of non-zero elements from the array [1, 2, 0, 0, 4, 0].

import numpy as np

array = np.array([1, 2, 0, 0, 4, 0])
non_zero_indices = np.nonzero(array)
print(non_zero_indices)
