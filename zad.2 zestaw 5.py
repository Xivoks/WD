class Kwadrat():

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self):
        return self.x+self.y


kw = Kwadrat(5)
print(kw.__add__())
