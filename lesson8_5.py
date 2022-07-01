# x + 2y – z = 1
# 8x – 5y + 2z = 12
# z = x + 2y - 1
# 8x -5y + 2(x + 2y - 1) = 12
# 10x - y = 14
# y = 10x - 14
# z = x + 20x - 15 = 21x - 15

from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def q(x, y, z):
    return x ** 2 + y ** 2 + z ** 2


fig = figure()
ax = Axes3D(fig, auto_add_to_figure=False)
fig.add_axes(ax)
x = np.arange(-50, 50, 1)
y = np.arange(-50, 50, 1)
x, y = np.meshgrid(x, y)
ax.plot_surface(x, y, q(x, 10 * x - 14, 21 * x - 15))
show()

a = np.array([[1, 2, -1], [8, -5, 2]])
b = np.array([1, 12])
x2 = np.linalg.lstsq(a, b, rcond=None)
print(x2)
