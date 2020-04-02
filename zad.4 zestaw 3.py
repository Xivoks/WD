import math


def funkcja_monotonicznosc(a):
    if(a > 0):
        print("Funkcja jest rosnąca")
    elif(a == 0):
        print("Funkcja jest stała")
    else:
        print("Funkcja jest malejąca")


monotonicznosc = funkcja_monotonicznosc
monotonicznosc(4)
