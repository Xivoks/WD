import numpy as np


def generuj(dlugosc):
    # a = np.arange(dlugosc, 0, -1)
    diagonalna = np.diag([a for a in range(dlugosc, 0, -1)])
    return diagonalna


print(generuj(3))
