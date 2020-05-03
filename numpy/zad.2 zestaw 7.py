import numpy as np
a = np.arange(9).reshape(3, 3)
b = np.arange(16).reshape(4, 4)
print("minimalna rzędów", a.min(axis=1))
print("minimalna kolumn", a.min(axis=0))
print(a)
print("minimalna rzędów", b.min(axis=1))
print("minimalna kolumn", b.min(axis=0))
print(b)
