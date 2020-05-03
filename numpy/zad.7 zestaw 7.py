import numpy as np
a = np.arange(6).reshape(2, 3)
b = np.cos(a)
c = np.sin(a)
print(np.add(b, c))
