class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x = x
        self.y = y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x

    def __str__(self):
        return 'Kwadrat o boku {}'.format(self.x)

    def __add__(self, other):
        iksy = self.x+other.x
        return Kwadrat(iksy)

    def __ge__(self, other):  # a>=b
        if self.x >= other.x:
            return True
        return False

    def __gt__(self, other):  # a>b
        if self.x > other.x:
            return True
        return False

    def __le__(self, other):  # a<=b
        if self.x <= other.x:
            return True
        return False

    def __lt__(self, other):  # a<b
        if self.x < other.x:
            return True
        return False


kw1 = Kwadrat(3)
print(kw1)
kw2 = Kwadrat(5)
print(kw2)
kw3 = kw1+kw2
kw4 = Kwadrat(3)
print(kw3)
print(kw1 >= kw2)
print(kw2 >= kw1)
print(kw4 >= kw1)
print(kw1 >= kw4)
print("")
print(kw1 > kw2)
print(kw2 > kw1)
print(kw4 > kw1)
print(kw1 > kw4)
print("")
print(kw1 <= kw2)
print(kw2 <= kw1)
print(kw4 <= kw1)
print(kw1 <= kw4)
print("")
print(kw1 < kw2)
print(kw2 < kw1)
print(kw4 < kw1)
print(kw1 < kw4)

if(kw1 < kw2):
    print(kw1, "mniejszy od ", kw2)
