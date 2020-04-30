import numpy as np


def wykreslanka():
    slowa = ['kiwi', 'iicp', 'lawo', 'iaii']
    a = np.array([[x for x in slowa[i]] for i in range(4)])
    return a


print(wykreslanka())
