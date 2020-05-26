import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(1, 20, 20)
plt.plot(x, 1/x, 'g--^', label='f(x)=1/x')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
