class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(self.rodzaj)


class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        Material.__init__(self, rodzaj, dlugosc, szerokosc)
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print(self.rozmiar, self.kolor, self.dla_kogo)


class Sweter(Ubrania):
    def __init__(self, rodzaj1, rozmiar, kolor, dla_kogo):
        self.rodzaj_swetra = rodzaj1
        Material.__init__(self, rodzaj, dlugosc, szerokosc)
        Ubrania.__init__(self, rozmiar, kolor, dla_kogo)
        self.kolor_z_ubrania = self.kolor

    def wyswietl_dane(self):
        print(self.rodzaj_swetra, self.kolor_z_ubrania)


a = Material("tkanina", 2, 4)
b = Ubrania("M", "czerwony", "Męskie")
c = Sweter("Golf", "M", "czerwony", "Męskie")
c.wyswietl_dane()
