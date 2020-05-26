import numpy as np
import matplotlib.pyplot as plt
import random
min = 1
max = 6


def funkcja(min, max):
    k = 0
    kappa = []
    while k < max:
        a = (random.randint(min, max))
        b = (random.randint(min, max))
        c = a+b
        kappa.insert(k, c)
        k += 1
    print(kappa)
    return(kappa)


abc = funkcja(min, max)
plt.hist(abc, bins=7, facecolor='g', alpha=0.75, density=True)


plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
# wyświatlanie siatki
plt.grid(True)
plt.show()
