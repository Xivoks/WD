def wzor(a1=1, r=1, ile=1):
    wyraz = a1+((ile-1)*r)
    return(wyraz)


def suma(a1=1, r=1, ile=10):
    suma_ciagu = (((2*a1)+((ile-1)*r))*0.5)*ile
    return(suma_ciagu)


ref = suma
ref(1, 2, 4)
