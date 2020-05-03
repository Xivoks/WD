import numpy as np

a = np.arange(12)
b = a.reshape(3, 4)
c = a.reshape(4, 3)
d = a.reshape(2, 6)
print(a, "\n\n", b, "\n\n", c, "\n\n", d)
b = b.ravel()
c = c.ravel()
d = d.ravel()
print(a, "\n\n", b, "\n\n", c, "\n\n", d)
# są identyczne
