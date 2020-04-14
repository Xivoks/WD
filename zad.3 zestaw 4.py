import sys
with open("zadanie3_zestaw4.txt", "a+") as plik:
    for i in range(10):
        plik.write("Linia%d\r\n" % (i+1))
with open("zadanie3_zestaw4.txt", "r") as plik:
    tekst = plik.readlines()
    print(tekst)
