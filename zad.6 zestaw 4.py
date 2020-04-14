class slowa:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x = x
        self.y = y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def czy_palindrom(self):
        self.wyraz = self.y
        self.wyraz = self.wyraz.casefold()
        self.odwrocony_wyraz = reversed(self.wyraz)
        if list(self.wyraz) == list(self.odwrocony_wyraz):
            print("Ten wyraz jest palindromem.")
        else:
            print("Ten wyraz jest nie palindromem")

    def czy_metagramy(self):
        self.wyraz = self.x
        self.wyraz1 = self.y
        self.dl1 = len(self.wyraz)
        self.dl2 = len(self.wyraz1)
        self.wynik = 0
        if(self.dl1 == self.dl2):
            for self.i in range(0, self.dl1, 1):
                if self.wyraz[self.i] == self.wyraz1[self.i]:
                    self.wynik += 0
                else:
                    self.wynik += 1
        if (self.wynik == 1):
            print("to są metagramy")
        else:
            print("to nie sa metagramy")

    def czy_anagramy(self):
        self.wyraz = self.x
        self.wyraz1 = self.y
        self.dl1 = len(self.wyraz)
        self.dl2 = len(self.wyraz1)
        for i in range(self.dl1):
            a = 0
            for j in range(self.dl2):
                if self.wyraz[i] == self.wyraz1[j]:
                    a = a+1
                if j == len(self.wyraz1)-1 and a == 0:
                    return "nie, to nie sa anagramy"
        return "tak, są to anagramy"

    def wyswietl_wyrazy(self):
        self.wyraz = self.x
        self.wyraz1 = self.y
        print("Słowo 1:", self.wyraz, " Słowo 2:", self.wyraz1)


zbior_slow = slowa("tama", "mata")
zbior_slow.czy_palindrom()
zbior_slow.czy_metagramy()
print(zbior_slow.czy_anagramy())
zbior_slow.wyswietl_wyrazy()
