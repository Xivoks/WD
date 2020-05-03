import numpy as np
# generujemy macierz 9x9
b = np.arange(81).reshape(9, 9)
print(b)
print(b.shape)
# w macierzy 9x9 jest 81 "pól", macierz możemy przekształcić jezeli nowa macierz będzie zawierała tyle samo pól
c = b.reshape((3, 27))
print(c)
print(c.shape)
d = b.reshape((27, 3))
print(d)
print(d.shape)
