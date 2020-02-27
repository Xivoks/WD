print("Hello world!")

tekst="Hello world!"
print(tekst)
print(type(tekst))
print(type(5))
print(type(True))
print(5+5)
print(5-5)
print(5*5)
print(5/5)
print(5//5) #dzielenie bez reszty
print(5%5)  #modulo
print(5**5) #potegowanie
print("Ala "+"ma kota.")#konkatenacja
# print("Ala"+"ma"+5+"lat")#błąd
print("Ala "+"ma "+str(5)+" lat")
liczba=int("100")
print("Ala "*10)
#listy
lista=[]
print(type(lista))
lista2=[1,2,3]
print(lista2[0])
imie="Magdalena"
print(imie[0])
lista2[0]=5
# imie[0]="K" #błąd 
print(imie.swapcase()) #tylko wyswietlenie
imie = imie.swapcase() #nadpisanie
print(imie)
"Ala".swapcase()
lista3=[1, "Ala", 4.5, None, True,[1, 2]]
lista3[5][1]
macierz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]

]
macierz[1][1] #5
nowa= lista2 + macierz


#słownik
slownik = {}
slownik['imie'] = 'Adam'
slownik[0] = 'Adam'
print(slownik)
slownik2={'imie': 'Adam', 0: 'Adam'}
print(slownik2.values())
print(slownik2.keys())

def pow():
    pass
from math import * 
import math as m 
from math import pow 
m.pi


#Zadania
pierwsza_zmienna="pierwszazmienna"
druga_zmienna="drugazmienna"
trzecia_zmienna=1
czwarta_zmienna=2
piata_zmienna=True
szosta_zmienna=False
siodma_zmienna=4.5
osma_zmienna=2.8
print(pierwsza_zmienna+druga_zmienna)

z=3
z+=1
print(z)
z-=1
print(z)
z*=2
print(z)
z/=2
print(z)
z**=2
print(z)
z%=2
print(z)