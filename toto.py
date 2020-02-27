#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
liczba = random.randint(1, 10)
# print("wylosowana liczba to: ", liczba)
for i in range(3):
    print("Próba: ", i+1)
    odp = input("Jaką liczbę od 1 do 10 mam na myśli? ")
    # print("Podałeś liczbe: ", odp)
    if liczba == int(odp):
        print("Zgadłeś! Dostajesz nagrode!")
        break
    elif i == 2:
        print("Miałem na myśli liczbę ", liczba)
    else:
        print("Nie zgadłeś! Spróbuj jeszcze raz.")
        print()
