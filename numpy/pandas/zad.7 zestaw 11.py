import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
np.random.seed(19680801)


def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 20

for c, m, zlow, zhigh in [('r', 'o', 0, 5)]:
    xs = randrange(n, 0, 5)
    ys = randrange(n, 0, 5)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
t = np.linspace(0, 5, 5)
z = t
x = t
y = t
ax.plot(x, y, z, label='zadanie 1')
ax.legend()
plt.show()
