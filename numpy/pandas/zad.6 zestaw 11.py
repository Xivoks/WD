import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure()
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

t = np.linspace(0, 5, 5)
z = t
x = t
y = t
ax1.plot(x, y, z, label='zadanie 1')
ax1.legend()



def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


n = 20
for c, m, zlow, zhigh in [('r', 'o', 0, 5)]:
    xs = randrange(n, 0, 5)
    ys = randrange(n, 0, 5)
    zs = randrange(n, zlow, zhigh)
    ax2.scatter(xs, ys, zs, c=c, marker=m)

ax2.set_xlabel('X Label')
ax2.set_ylabel('Y Label')
ax2.set_zlabel('Z Label')
plt.show()
