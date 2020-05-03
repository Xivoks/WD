import numpy as np
a = np.arange(3, dtype=float).reshape(1, 3)
b = np.arange(1, 6, 2).reshape(1, 3)
print(a*b)
