def wzor(a1=1, q=1, ile=1):
    wyraz = a1*q**ile
    return(wyraz)


def suma(a1=1, q=1, ile=10):
    suma_ciagu = a1
    for x in range(1, ile):
        suma_ciagu += a1*(q**x)
    return(suma_ciagu)
