import math


def suma_ciagu(a1=1, r=1, ile=10):
    suma = 0
    for x in range(a1, ile, r):
        suma += x
    print(suma)


ciag = suma_ciagu
ciag()
