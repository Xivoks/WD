# class parzyste:
#     def __init__(self, data):
#         self.data = data
#         self.index = -2

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.index += 2
#         if self.index >= len(self.data):
#             raise StopIteration
#         return self.data[self.index]


# slowo = parzyste("Kamil")
# it = iter(slowo)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

def parzyste(data):
    for ind in range(0, len(data), 2):
        yield data[ind]


slowo = parzyste("Kamil")
print(next(slowo))
print(next(slowo))
print(next(slowo))
