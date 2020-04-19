class samogloski:
    __samogloski = {"a", "e", "y", "i", "o", "u"}

    def __init__(self, data):
        if isinstance(data, str):
            self.data = data
        else:
            self.data = str(data)
        self.ind = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.ind += 1
        if self.ind >= len(self.data):
            raise StopIteration
        if self.data[self.ind] in samogloski.__samogloski:
            return self.data[self.ind]


wejscie = samogloski("Kapiszon")
it = iter(wejscie)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
