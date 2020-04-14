class ciagi:
    def __init__(self, x1, n, r):
        self.x1 = x1
        self.n = n
        self.r = r

    def wyświetl_dane(self):
        for i in range(0, self.n, 1):
            print(self.x1+(i*self.r))

    def pobierz_elementy(self, y1, y2, y3):
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3

    def pobierz_parametry(self, x1, n, r):
        self.y1 = x1
        self.yn = n
        self.yr = r

    def policz_sume(self):
        return (((2*self.x1+((self.n-1)*self.r))*0.5))*self.n

    def policz_elementy(self, x1, r, xn):
        self.y1 = x1
        self.yr = r
        self.yn = xn
        self.i = 0
        while(self.yn > 0):
            self.yn -= self.yr
            self.i += 1
        print(self.i)


jakies = ciagi(2, 8, 2)
jakies.wyświetl_dane()
jakies.pobierz_elementy(2, 5, 8)
print(jakies.policz_sume())
jakies.policz_elementy(2, 2, 10)
