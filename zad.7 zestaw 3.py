import math


def pitagoras(a=3, b=4):
    c = a**2+b**2
    dl_c = math.sqrt(c)
    print(dl_c)


pita = pitagoras
pita()
