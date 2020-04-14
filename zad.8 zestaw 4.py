class Robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        self.y = self.y+self.krok*ile_krokow

    def idz_w_dol(self, ile_krokow):
        self.y = self.y-self.krok*ile_krokow

    def idz_w_prawo(self, ile_krokow):
        self.x = self.x+self.krok*ile_krokow

    def idz_w_lewo(self, ile_krokow):
        self.x = self.x-self.krok*ile_krokow

    def gdzie(self):
        return self.x, self.y


obiekt = Robaczek(4, 0, 6)
obiekt.idz_w_dol(4)
print(obiekt.gdzie())
obiekt.idz_w_prawo(12)
print(obiekt.gdzie())
del(obiekt)
