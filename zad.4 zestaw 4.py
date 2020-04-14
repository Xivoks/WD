class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        return self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed

    def ile_produktu(self):
        return(str(self.ilosc)+self.jednostka_miary)

    def ile_kosztuje(self):
        return self.ilosc*self.cena_jed


kappa = NaZakupy("chleb", 2, "szt", 2)
print(kappa.wyswietl_produkt())
print(kappa.ile_produktu())
print(kappa.ile_kosztuje())
