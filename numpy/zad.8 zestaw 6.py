import numpy as np


def foo(tablica, kierunek):
    czy = True
    if kierunek == "vertical":
        if tablica.shape[1] % 2 == 0:
            c = int(tablica.shape[1]/2)
            tablica1 = tablica[:, :c]
            tablica2 = tablica[:, c:]
        else:
            czy = False
    elif kierunek == "horizon":
        if tablica.shape[0] % 2 == 0:
            c = int(tablica.shape[0]/2)
            tablica1 = tablica[:c, :]
            tablica2 = tablica[c:, :]
        else:
            czy = False
    else:
        print("Invalid value!")
    if czy == True:
        return tablica1, tablica2
    else:
        print("Wymiary nie pozwalają na taki podział")
        return 0, 0


tablica = np.array([[y for y in range(x*6+1, x*6+6+1)] for x in range(0, 6)])
print(tablica)
b1, b2 = foo(tablica, "vertical")
print(b1)
print(b2)
b1, b2 = foo(tablica, "horizon")
print(b1)
print(b2)
tablica = np.array([[y for y in range(x*5+1, x*5+5+1)] for x in range(0, 5)])
print(tablica)
b1, b2 = foo(tablica, "vertical")
print(b1)
print(b2)
b1, b2 = foo(tablica, "horizon")
print(b1)
print(b2)
