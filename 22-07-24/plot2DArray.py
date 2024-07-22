# Create two 2-D arrays and Plot them using matplotlib.

import numpy as np
import matplotlib.pyplot as plt

array_1 = np.arange(2, 13, 2).reshape(3, 2)
array_2 = np.arange(1, 12, 2).reshape(3, 2)
fig, ax = plt.subplots()
ax.plot(array_1)
ax.plot(array_2)
plt.show()
