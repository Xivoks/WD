import numpy as np


def generuj(podstawa, ilosc):
    a = np.logspace(1, ilosc, num=ilosc, base=podstawa)
    return a


print(generuj(2, 4))
