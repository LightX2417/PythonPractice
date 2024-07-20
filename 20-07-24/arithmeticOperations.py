# Create a result array by adding the two NumPy arrays. Next, modify the result array by calculating the square of each element.

import numpy as np

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
result = a1 + a2
print(f"Result:\n{result}")
result *= result
print(f"Result:\n{result}")
