import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = range(1, 21)
y = [1/y for y in x]
plt.plot(x, y, label='f(x)=1/x')
plt.axis([1, len(x), 0, 1])
plt.xlabel('x')
plt.ylabel('f(x)')
plt.xticks(np.arange(0, 21, 1))
plt.yticks(np.arange(0, 1.1, 0.1))
plt.legend()

plt.show()
