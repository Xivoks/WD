import sys
lista = []
for x in range(4, 1500, 4):
    lista += [x]
plik = open("podzielne.txt", "a+")
plik.writelines(str(lista))
plik.close()
