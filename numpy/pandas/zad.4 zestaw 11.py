import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# konfiguracja wielkości wykresu, figsize określa wielkość wykresu w calach
fig = plt.figure(figsize=(10, 2))
ax1 = fig.add_subplot(151, projection='3d')
ax2 = fig.add_subplot(152, projection='3d')
ax3 = fig.add_subplot(153, projection='3d')
ax4 = fig.add_subplot(154, projection='3d')
ax5 = fig.add_subplot(155, projection='3d')

# fikcyjne dane
_x = np.arange(4)
_y = np.arange(5)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1
ax1.bar3d(x, y, bottom, width, depth, top, shade=True, edgecolor='y')

ax2.bar3d(x, y, bottom, width, depth, top, shade=True, color='black')

ax3.bar3d(x, y, bottom, width, depth, top, shade=True, color='r')

ax4.bar3d(x, y, bottom, width, depth, top, shade=True, color='purple')

ax5.bar3d(x, y, bottom, width, depth, top,
          shade=False, edgecolor='g', color='w')

plt.show()
