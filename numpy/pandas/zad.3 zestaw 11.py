from mpl_toolkits.mplot3d.axes3d import get_test_data
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import random


fig = plt.figure(figsize=plt.figaspect(0.2))

cmaps = [cm.viridis, cm.Purples, cm.autumn, cm.magma, cm.Blues, cm.Greys, cm.binary, cm.gist_yarg, cm.gist_gray,
         cm.gray, cm.bone, cm.pink, cm.spring, cm.summer, cm.autumn, cm.flag, cm.prism, cm.CMRmap, cm.cubehelix, cm.brg, cm.hsv]
for liczba in range(1, 6, 1):
    ax = fig.add_subplot(1, 5, liczba, projection='3d')
    a = (random.randint(0, 22))
    X = np.arange(- 5, 5, 0.25)
    Y = np.arange(- 5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    surf = ax.plot_surface(
        X, Y, Z, cmap=cmaps[a], linewidth=0, antialiased=False)
    ax.set_zlim(- 1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    # Dodanie paska kolorów.
    fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
