# Sort a 2-dimensional array by
# a. Second row
# b. Second column

import numpy as np

array = np.array([[6, 5, 4], [3, 2, 1]])
print(f"Original array:\n{array}")
array = array[:, array[1, :].argsort()]
print(f"Array sorted by second row:\n{array}")
array = array[array[:, 1].argsort()]
print(f"Array sorted by second column:\n{array}")
